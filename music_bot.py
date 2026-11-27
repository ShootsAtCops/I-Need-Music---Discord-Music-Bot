"""
Discord Music Bot - Plays music from any source URL
Supports: YouTube, SoundCloud, Spotify, and more via yt-dlp
Features:
1. Play music from any URL
2. Queue system for multiple songs
3. Insert songs at the top of queue
4. Clear all queue function
"""

import discord
from discord.ext import commands, tasks
import yt_dlp
import asyncio
import os
from datetime import timedelta
import logging
import re

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configure yt-dlp options
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': '%(title)s.%(ext)s',
    'quiet': True,
    'no_warnings': False,
    'cookiefile': 'cookies.txt' if os.path.exists('cookies.txt') else None,
}

# Intents for the bot
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

# Global variables for bot state
class MusicBot(commands.Bot):
    def __init__(self, token):
        super().__init__(
            command_prefix='\\',  # Use backslash as command prefix
            intents=intents,
            case_insensitive=True
        )
        self.token = token
        
        # Queue management (per guild)
        self.queues = {}  # guild_id -> list of (url, title, duration)
        self.current_playing = {}  # guild_id -> ydl object
        self.playing_tasks = {}  # guild_id -> asyncio.Task
        self.voice_clients = {}  # guild_id -> VoiceClient
        
    async def on_ready(self):
        logger.info(f'Logged in as {self.user} (ID: {self.user.id})')
        logger.info(f'Discord API version: {discord.__version__}')
        
        # Start periodic cleanup task
        if not self.cleanup_task.running:
            self.cleanup_task.start()
    
    async def process_url(self, guild_id, url):
        """Process a URL and extract audio"""
        try:
            info = await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: yt_dlp.YoutubeDL(ydl_opts).extract_info(url, download=False)
            )
            
            title = info.get('title', 'Unknown Title')
            duration = info.get('duration', 0)
            thumbnail = info.get('thumbnail', [{}])[0].get('url', '') if info.get('thumbnail') else ''
            
            return {
                'url': url,
                'title': title,
                'duration': duration,
                'thumbnail': thumbnail,
                'ydl_info': info
            }
        except Exception as e:
            logger.error(f"Error processing URL: {e}")
            raise
    
    async def download_and_stream(self, guild_id, url):
        """Download and stream audio to voice channel"""
        try:
            # Get voice client
            vc = self.voice_clients[guild_id]
            
            # Process URL
            info = await self.process_url(guild_id, url)
            title = info['title']
            duration = info['duration']
            thumbnail = info['thumbnail']
            ydl_info = info['ydl_info']
            
            # Create download path
            ydl_path = f"./{title.replace(' ', '_').replace('[', '').replace(']', '')}.mp3"
            
            # Download the audio
            logger.info(f"Downloading: {title}")
            await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: yt_dlp.YoutubeDL(ydl_opts).download([url])
            )
            
            # Open audio file
            if os.path.exists(ydl_path):
                source = discord.FFmpegPCMAudio(ydl_path, position=None)
                
                # Send song to voice channel
                await vc.play(source, after=lambda: self.stop_playing(guild_id))
                
                logger.info(f"Playing: {title}")
            else:
                logger.error(f"Download failed for: {title}")
                raise Exception("Download failed")
                
        except Exception as e:
            logger.error(f"Error streaming audio: {e}")
            raise
    
    async def stop_playing(self, guild_id):
        """Stop current playback and cleanup"""
        if guild_id in self.playing_tasks:
            task = self.playing_tasks[guild_id]
            if not task.done():
                task.cancel()
            del self.playing_tasks[guild_id]
        
        if guild_id in self.current_playing:
            del self.current_playing[guild_id]
    
    @tasks.loop(seconds=30)
    async def cleanup_task(self):
        """Periodic cleanup of disconnected voice clients"""
        for guild_id, vc in list(self.voice_clients.items()):
            if not vc.is_connected():
                try:
                    await vc.disconnect()
                    del self.voice_clients[guild_id]
                    # Clear queue and stop playing
                    if guild_id in self.queues:
                        del self.queues[guild_id]
                    if guild_id in self.current_playing:
                        del self.current_playing[guild_id]
                except Exception as e:
                    logger.error(f"Error disconnecting voice client: {e}")
    
    @commands.Cog()
    class MusicCog(commands.Cog):
        def __init__(self, bot):
            self.bot = bot
        
        async def check_permissions(self, ctx):
            """Check if user has permission to use music commands"""
            member = ctx.guild.get_member(ctx.author.id)
            if not member:
                return False
            
            # Check if user is in voice channel
            vc = ctx.guild.voice_client
            if not vc or len(vc.channel.members) == 0:
                await ctx.send("❌ You must be in a voice channel to use music commands!")
                return False
            
            return True
        
        @commands.command(name='play', description='Play music from URL or search')
        async def play(self, ctx, *, query: str):
            """Play a song from URL or search keyword"""
            if not await self.check_permissions(ctx):
                return
            
            # Get current guild ID
            guild_id = ctx.guild.id
            
            # Initialize queue if needed
            if guild_id not in self.queues:
                self.queues[guild_id] = []
            
            # Check if already playing
            if guild_id in self.current_playing:
                await ctx.send("🎵 A song is already playing! Adding to queue.")
                return
            
            # Join voice channel
            try:
                vc = await ctx.author.voice.channel.connect()
                self.voice_clients[guild_id] = vc
            except discord.errors.Disconnect as e:
                await ctx.send("❌ Error connecting to voice channel!")
                logger.error(f"Voice connect error: {e}")
                return
            
            # Check if query is a URL
            is_url = self.is_valid_url(query)
            
            try:
                if is_url:
                    # Direct URL play
                    song = await self.download_and_stream(guild_id, query)
                    title = song['title']
                    duration = song['duration']
                    thumbnail = song['thumbnail']
                else:
                    # Search for the query
                    search_results = await self.search_query(ctx, query)
                    if not search_results:
                        await ctx.send("❌ No results found!")
                        return
                    
                    # Pick first result or ask user to choose
                    first_result = search_results[0]
                    song = await self.download_and_stream(guild_id, first_result['url'])
                    title = song['title']
                    duration = song['duration']
                    thumbnail = song['thumbnail']
                
                # Add to queue and play
                self.queues[guild_id].append({
                    'url': query if is_url else first_result['url'],
                    'title': title,
                    'duration': duration,
                    'thumbnail': thumbnail
                })
                
                # Update current playing
                self.current_playing[guild_id] = {
                    'title': title,
                    'duration': duration,
                    'thumbnail': thumbnail,
                    'index': 0
                }
                
                await ctx.send(
                    f"✅ **Now Playing:** {title}\n"
                    f"⏱️ Duration: {timedelta(seconds=duration)}\n"
                    f"🎶 Queue: {len(self.queues[guild_id]) - 1} more songs"
                )
                
            except Exception as e:
                logger.error(f"Error playing song: {e}")
                await ctx.send(f"❌ Error playing music: {str(e)}")
        
        @commands.command(name='queue', description='Show current queue')
        async def queue(self, ctx):
            """Display the current song queue"""
            guild_id = ctx.guild.id
            
            if guild_id not in self.queues or len(self.queues[guild_id]) == 0:
                await ctx.send("📭 **Queue is empty!**")
                return
            
            # Get current song info
            current = self.current_playing.get(guild_id)
            current_title = current['title'] if current else "No song playing"
            
            queue_items = self.queues[guild_id]
            queue_text = f"📋 **Queue ({len(queue_items)} songs):**\n\n"
            
            for i, item in enumerate(queue_items):
                duration_str = "⏱️ Unknown" if item['duration'] == 0 else f"⏱️ {timedelta(seconds=item['duration'])}"
                queue_text += f"{i+1}. **{item['title']}**\n{duration_str}\n\n"
            
            await ctx.send(
                f"🎵 **Currently Playing:** {current_title}\n"
                f"{queue_text}"
            )
        
        @commands.command(name='insert', description='Insert song at top of queue')
        async def insert(self, ctx, *, query: str):
            """Insert a song at the top of the queue"""
            if not await self.check_permissions(ctx):
                return
            
            guild_id = ctx.guild.id
            
            # Initialize queue if needed
            if guild_id not in self.queues:
                self.queues[guild_id] = []
            
            try:
                # Process the URL
                song = await self.process_url(guild_id, query)
                title = song['title']
                duration = song['duration']
                thumbnail = song['thumbnail']
                
                # Insert at the beginning of queue
                self.queues[guild_id].insert(0, {
                    'url': query,
                    'title': title,
                    'duration': duration,
                    'thumbnail': thumbnail
                })
                
                await ctx.send(
                    f"✅ **Inserted at top of queue:** {title}\n"
                    f"⏱️ Duration: {timedelta(seconds=duration)}\n"
                    f"🎶 Total queue: {len(self.queues[guild_id])} songs"
                )
                
            except Exception as e:
                logger.error(f"Error inserting song: {e}")
                await ctx.send(f"❌ Error inserting song: {str(e)}")
        
        @commands.command(name='skip', description='Skip current song')
        async def skip(self, ctx):
            """Skip the currently playing song"""
            if not await self.check_permissions(ctx):
                return
            
            guild_id = ctx.guild.id
            
            if guild_id not in self.current_playing:
                await ctx.send("❌ No song is currently playing!")
                return
            
            try:
                # Stop current playback
                if guild_id in self.playing_tasks and not self.playing_tasks[guild_id].done():
                    self.playing_tasks[guild_id].cancel()
                
                await ctx.send("⏭️ **Skipped!** Playing next song...")
                
            except Exception as e:
                logger.error(f"Error skipping song: {e}")
                await ctx.send(f"❌ Error skipping: {str(e)}")
        
        @commands.command(name='clear', description='Clear all songs in queue')
        async def clear(self, ctx):
            """Clear all songs from the queue"""
            if not await self.check_permissions(ctx):
                return
            
            guild_id = ctx.guild.id
            
            if guild_id not in self.queues or len(self.queues[guild_id]) == 0:
                await ctx.send("📭 **Queue is already empty!**")
                return
            
            original_length = len(self.queues[guild_id])
            self.queues[guild_id] = []
            
            # Clear current playing if it's in the queue
            if guild_id in self.current_playing:
                del self.current_playing[guild_id]
            
            await ctx.send(
                f"🗑️ **Cleared {original_length} song(s) from queue!**\n"
                f"📭 Queue is now empty."
            )
        
        @commands.command(name='stop', description='Stop music and disconnect')
        async def stop(self, ctx):
            """Stop music and disconnect from voice channel"""
            if not await self.check_permissions(ctx):
                return
            
            guild_id = ctx.guild.id
            
            try:
                # Clear queue
                if guild_id in self.queues:
                    del self.queues[guild_id]
                
                # Stop playing
                if guild_id in self.current_playing:
                    del self.current_playing[guild_id]
                
                # Disconnect voice client
                vc = self.voice_clients.get(guild_id)
                if vc:
                    await vc.disconnect()
                    del self.voice_clients[guild_id]
                
                await ctx.send("🛑 **Stopped and disconnected!**")
                
            except Exception as e:
                logger.error(f"Error stopping: {e}")
                await ctx.send(f"❌ Error stopping: {str(e)}")
        
        @commands.command(name='nowplaying', description='Show currently playing song')
        async def nowplaying(self, ctx):
            """Display currently playing song information"""
            guild_id = ctx.guild.id
            
            if guild_id not in self.current_playing:
                await ctx.send("🎵 No song is currently playing!")
                return
            
            current = self.current_playing[guild_id]
            title = current['title']
            duration = current['duration']
            thumbnail = current['thumbnail']
            
            duration_str = "⏱️ Unknown" if duration == 0 else f"⏱️ {timedelta(seconds=duration)}"
            
            embed = discord.Embed(
                title="🎵 Now Playing",
                description=title,
                color=discord.Color.blue()
            )
            
            embed.add_field(name="Duration", value=duration_str, inline=True)
            embed.set_thumbnail(url=thumbnail if thumbnail else "https://via.placeholder.com/150")
            
            await ctx.send(embed=embed)
        
        def is_valid_url(self, url):
            """Check if the query is a valid URL"""
            patterns = [
                r'https?://[^\s]+',  # HTTP/HTTPS URLs
                r'youtu\.be/',  # YouTube short URLs
                r'soundcloud\.com/',  # SoundCloud URLs
                r'spotify\.com/',  # Spotify URLs
            ]
            
            for pattern in patterns:
                if re.search(pattern, url):
                    return True
            return False
        
        async def search_query(self, ctx, query):
            """Search YouTube for a query and return results"""
            try:
                # Simple YouTube search (yt-dlp can do this)
                search_opts = ydl_opts.copy()
                search_opts['quiet'] = False
                search_opts['no_warnings'] = True
                
                info = await asyncio.get_event_loop().run_in_executor(
                    None,
                    lambda: yt_dlp.YoutubeDL(search_opts).extract_info(
                        f"https://www.youtube.com/results?search_query={query}",
                        download=False
                    )
                )
                
                # Parse playlist info
                if 'entries' in info:
                    results = []
                    for entry in info['entries'][:5]:  # Get top 5
                        title = entry.get('title', 'Unknown')
                        url = entry.get('url', '')
                        duration = entry.get('duration', 0)
                        thumbnail = entry.get('thumbnail', [{}])[0].get('url', '') if entry.get('thumbnail') else ''
                        results.append({
                            'title': title,
                            'url': url,
                            'duration': duration,
                            'thumbnail': thumbnail
                        })
                    return results
                
            except Exception as e:
                logger.error(f"Search error: {e}")
            
            return []
    
    async def setup_hook(self):
        """Setup cog when bot is ready"""
        await self.add_cog(MusicCog(self))

# Create bot instance and start
def run_bot(token):
    bot = MusicBot(token)
    bot.run(token)

if __name__ == '__main__':
    # Replace with your Discord bot token
    TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
    
    if TOKEN == 'YOUR_DISCORD_BOT_TOKEN':
        print("❌ Please replace 'YOUR_DISCORD_BOT_TOKEN' with your actual Discord bot token!")
        print("\nGet your token from: https://discord.com/developers/applications")
    else:
        run_bot(TOKEN)
