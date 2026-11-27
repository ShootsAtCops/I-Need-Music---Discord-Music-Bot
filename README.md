# 🎵 Discord Music Bot

A powerful Discord music bot that plays music from **any source URL** including YouTube, SoundCloud, Spotify, and more!

## ✨ Features

### 1. **Play Any Song via Link** 🎶
   - Play music from YouTube, SoundCloud, Spotify, and hundreds of other sources
   - Works with direct URLs or search keywords
   - Automatic audio extraction and streaming

### 2. **Queue System** ⏱️
   - Songs added after the first one automatically go into a queue
   - View the entire queue with song titles and durations
   - See what's currently playing

### 3. **Insert at Top** 📌
   - Add songs to the **top of the queue** using `\insert` command
   - Perfect for prioritizing favorite songs

### 4. **Clear Queue** 🗑️
   - Clear all songs from the queue instantly
   - Stop and disconnect from voice channel

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- Discord Bot Token (free from [Discord Developer Portal](https://discord.com/developers/applications))
- FFmpeg installed on your system (required for audio processing)

### Step 1: Create a Discord Bot
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to the "Bot" section
4. Click "Add Bot" and confirm
5. Under "Token", click "Copy" to get your bot token
6. Enable "MESSAGE CONTENT INTENT" under Privileged Gateway Intents
7. Invite your bot to your server using this URL (replace TOKEN):
   ```
   https://discord.com/api/oauth2/authorize?client_id=TOKEN&permissions=8&scope=bot%20applications.commands
   ```

### Step 2: Install Dependencies
```bash
# Create a virtual environment (recommended)
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

### Step 3: Configure the Bot
1. Open `music_bot.py`
2. Replace `'YOUR_DISCORD_BOT_TOKEN'` with your actual bot token
3. Save the file

### Step 4: Download Cookies (Optional but Recommended)
Some videos require cookies to play, especially age-restricted content.

**How to get cookies:**
1. Install [Get cookies.txt](https://chrome.google.com/webstore/detail/get-cookiestxt/oknfoidjnjfofmieeigfakfgkkkeffeb) Chrome extension
2. Go to YouTube
3. Click the extension icon and export cookies as `cookies.txt`
4. Place `cookies.txt` in the same folder as `music_bot.py`

## 🎮 Usage Commands

### `\play <URL or keyword>`
Play a song from a URL or search for it.
```
\play https://www.youtube.com/watch?v=dQw4w9WgXcQ
\play Never Gonna Give You Up
\play https://soundcloud.com/user/track-name
\play https://open.spotify.com/track/abc123
```

### `\queue`
Display the current song queue with all songs waiting to be played.
```
\queue
```

### `\insert <URL or keyword>`
Insert a song at the **top** of the queue (before currently playing song).
```
\insert https://www.youtube.com/watch?v=your-video-id
\insert Top Hits Playlist
```

### `\clear`
Clear all songs from the queue.
```
\clear
```

### `\skip`
Skip the currently playing song and move to the next in queue.
```
\skip
```

### `\stop`
Stop music and disconnect the bot from the voice channel.
```
\stop
```

### `\nowplaying`
Show information about the currently playing song (title, duration, thumbnail).
```
\nowplaying
```

## 📋 Supported Sources

This bot uses **yt-dlp** which supports hundreds of sites:

- ✅ YouTube & YouTube Music
- ✅ SoundCloud
- ✅ Spotify
- ✅ Twitch
- ✅ Bandcamp
- ✅ Deezer
- ✅ Pandora
- ✅ And 500+ more!

See the full list at: https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md

## 🔧 Advanced Configuration

### Custom FFmpeg Settings
You can modify audio quality in `music_bot.py`:

```python
ydl_opts = {
    'format': 'bestaudio/best',  # Change format preference
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',  # Output format (mp3, wav, etc.)
        'preferredquality': '192',  # Audio quality (0-320)
    }],
}
```

### Voice Channel Requirements
The bot requires the following permissions:
- Connect to voice channels
- Speak in voice channels
- Read messages
- Send messages

## 🐛 Troubleshooting

### "Sign in to confirm you're not a bot" Error
This error occurs when YouTube detects bot-like behavior. Solutions:
1. Download and use `cookies.txt` file (see installation)
2. Use a Google account logged in to your browser before exporting cookies
3. Wait 24 hours - sometimes it's temporary

### FFmpeg Not Found
Make sure FFmpeg is installed and added to your system PATH.

**Windows:**
1. Download from: https://ffmpeg.org/download.html
2. Extract and add the `bin` folder to your PATH environment variable

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt-get install ffmpeg  # Ubuntu/Debian
sudo yum install ffmpeg       # Fedora/CentOS
```

### Queue Issues
If songs aren't queuing properly:
1. Make sure you're in the same voice channel as the bot
2. Check that the URL is valid and accessible
3. Verify yt-dlp can download from the source

## 📦 Project Structure
```
music_bot/
├── music_bot.py        # Main bot code
├── requirements.txt    # Python dependencies
├── cookies.txt         # YouTube cookies (optional)
└── README.md          # This file
```

## 🌟 Supported Commands Summary

| Command | Description |
|---------|-------------|
| `play` | Play song from URL or search |
| `queue` | Show current queue |
| `insert` | Add song to top of queue |
| `ear` | Clear all queue songs |
| `skip` | Skip current song |
| `stop` | Stop and disconnect |
| `/nowplaying` | Show currently playing info |

## 📝 Example Usage

**User in voice channel:**
```
User: play Linkin Park - Numb
Bot: ✅ Now Playing: Linkin Park - Numb
     ⏱️ Duration: 04:38
     🎶 Queue: 0 more songs

User: play https://soundcloud.com/example/track
Bot: ✅ Inserted at top of queue: Example Track
     ⏱️ Duration: 03:45
     🎶 Total queue: 1 songs

User: queue
Bot: 🎵 Currently Playing: Linkin Park - Numb
    
📋 Queue (2 songs):

1. **Example Track**
⏱️ 03:45

2. **Another Song**
⏱️ 05:12
```

## 🛡️ Security Notes
- Keep your bot token private! Never share it publicly
- Store your token in an environment variable for production:
  ```bash
  export DISCORD_TOKEN="your-token-here"
  ```
- Use `.gitignore` to prevent committing your token

## 🤝 Contributing
Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License
This project is licensed under the MIT License - see LICENSE file for details.

## 💬 Support
If you encounter any issues:
1. Check the troubleshooting section above
2. Review yt-dlp documentation: https://github.com/yt-dlp/yt-dlp
3. Open an issue on GitHub

---

**Made with ❤️ using discord.py and yt-dlp**