# 🎵 Discord Music Bot - Example Usage Guide

## Quick Start Commands

### 1. Playing Music
```bash
# Play a YouTube video by URL
\play https://www.youtube.com/watch?v=dQw4w9WgXcQ

# Search for a song
\play Linkin Park - Numb

# Play from SoundCloud
\play https://soundcloud.com/user/track-name

# Play from Spotify
\play https://open.spotify.com/track/abc123xyz
```

### 2. Queue Management
```bash
# View current queue
\queue

# Insert a song at the TOP of the queue (before currently playing)
\insert https://www.youtube.com/watch?v=your-video-id

# Clear all songs from queue
\clear

# Skip to next song
\skip
```

### 3. Playback Control
```bash
# Stop music and disconnect
\stop

# See what's currently playing
\nowplaying
```

## Example Conversation Flow

**Scenario: You want to play multiple songs in order**

1. **Start playing:**
   ```
   User: \play Linkin Park - Numb
   Bot: ✅ Now Playing: Linkin Park - Numb
       ⏱️ Duration: 04:38
       🎶 Queue: 0 more songs
   ```

2. **Add more songs to queue:**
   ```
   User: \play Eminem - Lose Yourself
   Bot: 🎵 A song is already playing! Adding to queue.
   
   User: \play Imagine Dragons - Believer
   Bot: 🎵 A song is already playing! Adding to queue.
   ```

3. **View the queue:**
   ```
   User: \queue
   Bot: 🎵 Currently Playing: Linkin Park - Numb
       
   📋 Queue (2 songs):
   
   1. **Eminem - Lose Yourself**
   ⏱️ 03:49
   
   2. **Imagine Dragons - Believer**
   ⏱️ 03:14
   ```

4. **Insert a favorite at the top:**
   ```
   User: \insert https://www.youtube.com/watch?v=your-favorite-video
   Bot: ✅ Inserted at top of queue: Your Favorite Song
       ⏱️ Duration: 05:23
       🎶 Total queue: 3 songs
   ```

5. **Clear everything:**
   ```
   User: \clear
   Bot: 🗑️ Cleared 3 song(s) from queue!
       📭 Queue is now empty.
   ```

## Important Notes

### ✅ Requirements Before Using:
1. You must be in a voice channel
2. The bot must be connected to the same voice channel
3. Have proper permissions (the invite link handles this)

### 🔔 How the Queue Works:
- **First song:** Plays immediately when you use `play`
- **Subsequent songs:** Automatically added to queue behind the current song
- **Insert command:** Adds a song at position 0 (top of queue, before current song)
- **Skip command:** Moves to the next song in queue
- **Clear command:** Removes all queued songs

### 🎯 Supported Sources:
The bot supports hundreds of sites through yt-dlp including:
- YouTube (videos, shorts, playlists)
- SoundCloud
- Spotify
- Twitch
- Bandcamp
- Deezer
- Pandora
- And 500+ more!

See full list: https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md

### ⚠️ Common Issues & Solutions:

**Issue: "Sign in to confirm you're not a bot"**
- **Solution:** Download and use `cookies.txt` file (see main README)

**Issue: "FFmpeg not found"**
- **Solution:** Install FFmpeg (see troubleshooting in main README)

**Issue: Song doesn't play but no error**
- **Solution:** Check if you're in the same voice channel as the bot

**Issue: Queue shows empty when it shouldn't be**
- **Solution:** Try `\queue` again, or use `\clear` then re-add songs

## Pro Tips

1. **Use cookies.txt** for better compatibility with age-restricted videos
2. **Insert command** is great for emergency favorites during a playlist
3. **Check queue** before using `\stop` to ensure you're not losing good songs
4. **Search keywords** work just like URLs - type what you want to find
5. **Voice channel permissions:** Make sure the bot has "Connect" and "Speak" permissions

## Testing Your Bot

1. Start the bot: `python music_bot.py`
2. Invite it to your Discord server
3. Join a voice channel with the bot
4. Try `\play` with a simple YouTube URL
5. Add more songs and check `\queue`
6. Test `\insert`, `\skip`, `\clear`, and `\stop`

## Need Help?

- Full documentation: See README.md
- yt-dlp support sites: https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md
- discord.py docs: https://discordpy.readthedocs.io/
- Troubleshooting: Check the main README.md file