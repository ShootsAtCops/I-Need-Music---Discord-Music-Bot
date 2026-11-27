# 🎵 Discord Music Bot - Complete Package

## What You Have

This is a **fully-featured Discord music bot** that can play music from ANY source URL including YouTube, SoundCloud, Spotify, and 500+ other sites!

⚡ **COMMAND PREFIX: Backslash (`\`) instead of Slash (`/`)**

---

## 📦 Files Included

### Core Files
1. **`music_bot.py`** - Main bot code with all features
2. **`requirements.txt`** - Python dependencies
3. **`test_bot.py`** - Pre-flight check script

### Documentation
4. **`README.md`** - Complete feature list and usage guide
5. **`INSTALLATION_GUIDE.md`** - Step-by-step installation instructions
6. **`USAGE_EXAMPLES.md`** - Example conversations and commands
7. **`QUEUE_SYSTEM_GUIDE.md`** - Visual queue system explanations
8. **`.gitignore`** - Protects your bot token from version control

---

## ✨ All Features Implemented

### ✅ 1. Play Any Song via Link
- Works with YouTube, SoundCloud, Spotify, and 500+ sites
- Accepts direct URLs or search keywords
- Automatic audio extraction and streaming
- Thumbnail display for songs

### ✅ 2. Queue System
- Songs added after the first go into a queue automatically
- View entire queue with titles and durations
- See what's currently playing separately
- Queue persists while bot is running

### ✅ 3. Insert at Top of Queue
- Add songs to the TOP of queue (before current song)
- Perfect for emergency favorites
- Uses `insert <URL>` command
- Maintains proper queue order

### ✅ 4. Clear All Queue Function
- Instantly clear all queued songs with `ear`
- Also clears currently playing song
- Start fresh anytime
- Cannot be undone (by design)

### 🎁 Bonus Features
- **Skip current song** - Move to next in queue
- **Stop and disconnect** - End session cleanly
- **Now Playing info** - See current song details
- **Automatic cleanup** - Handles disconnected voice channels
- **Multi-guild support** - Works across multiple servers
- **Slash commands** - Modern Discord command interface
- **Error handling** - Graceful error messages
- **Cookies support** - Plays age-restricted videos

---

## 🚀 Quick Start (5 Steps)

### 1. Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Get Discord Bot Token
- Go to: https://discord.com/developers/applications
- Create new application → Add bot → Copy token
- Enable "MESSAGE CONTENT INTENT"

### 3. Configure Bot
Edit `music_bot.py` and replace:
```python
TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
```

### 4. Test Setup
```bash
python test_bot.py
```
Expected: All checks should pass ✅

### 5. Run Bot
```bash
python music_bot.py
```
Bot is now running! Invite to your server and start using commands.

---

## 🎮 Command Cheat Sheet

| Command | Description | Example |
|---------|-------------|---------|
| `play` | Play song from URL or search | `play Linkin Park - Numb` |
| `queue` | Show current queue | `queue` |
| `insert` | Add song to TOP of queue | `insert https://youtube.com/watch?v=xyz` |
| `ear` | Clear all queue songs | `ear` |
| `skip` | Skip current song | `skip` |
| `stop` | Stop and disconnect | `stop` |
| `/nowplaying` | Show current song info | `/nowplaying` |

---

## 📚 Documentation Quick Links

- **Getting Started:** `INSTALLATION_GUIDE.md`
- **How to Use:** `USAGE_EXAMPLES.md`
- **Queue System:** `QUEUE_SYSTEM_GUIDE.md`
- **Full Features:** `README.md`

---

## 🔧 Supported Music Sources

This bot uses **yt-dlp** which supports hundreds of sites:

### Primary Support
- ✅ YouTube (videos, shorts, playlists)
- ✅ SoundCloud
- ✅ Spotify
- ✅ Twitch
- ✅ Bandcamp
- ✅ Deezer
- ✅ Pandora

### And 500+ More!
See full list: https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md

---

## 🛡️ Security Best Practices

1. **Never share your bot token** - Keep it private
2. **Use .gitignore** - Already included, prevents token commits
3. **Consider environment variables:**
   ```bash
   export DISCORD_TOKEN="your-token"
   ```
4. **Store tokens securely** - Use password managers
5. **Regular updates** - Keep dependencies updated

---

## 📊 System Requirements

### Minimum
- Python 3.8+
- FFmpeg installed
- Discord account
- Basic internet connection

### Recommended
- Python 3.10+
- Virtual environment
- cookies.txt for YouTube
- SSD storage (faster downloads)

---

## 🎯 Use Cases

### For Personal Use
- Play music in your Discord server with friends
- Build custom playlists on the fly
- Access any song from any source

### For Communities
- Music channels with queue management
- DJ-style insertion of favorites
- Clear queue for new sessions

### For Events
- Stream events from Twitch/YouTube
- Mix multiple sources seamlessly
- Emergency song insertion

---

## 🐛 Troubleshooting Quick Reference

| Problem | Solution |
|---------|----------|
| "Module not found" | Run `pip install -r requirements.txt` |
| FFmpeg errors | Install FFmpeg (see INSTALLATION_GUIDE.md) |
| Can't play videos | Download cookies.txt file |
| Bot not responding | Check permissions and intents |
| Queue issues | Try `ear` and rebuild queue |

---

## 📈 Future Enhancements (Not Included)

If you want to extend this bot:
- Add lyrics display
- Music visualization
- Playlist management
- Voting system for next song
- Premium quality audio
- Multiple voice channel support
- Custom emojis for commands
- Bot reactions for queue selection

---

## 🤝 Contributing

Want to improve this bot?
1. Report bugs in issues
2. Suggest features
3. Submit pull requests
4. Document new use cases

---

## 📞 Support Resources

- **yt-dlp Documentation:** https://github.com/yt-dlp/yt-dlp
- **discord.py Docs:** https://discordpy.readthedocs.io/
- **FFmpeg Docs:** https://ffmpeg.org/documentation.html
- **Discord Developer Portal:** https://discord.com/developers

---

## 🎉 Success Checklist

Before you start, make sure:
- [ ] Python 3.8+ installed
- [ ] FFmpeg installed and in PATH
- [ ] Discord bot created with token
- [ ] Bot invited to your server
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Token configured in `music_bot.py`
- [ ] Test script passed (`python test_bot.py`)
- [ ] Bot is running and visible in Discord

If all checked ✅, you're ready to go!

---

## 🎵 Start Playing Music!

```bash
# Run the bot
python music_bot.py

# In Discord:
play Your Favorite Song
queue  # See what's queued
insert Emergency Favorite  # Add to top
ear  # Start fresh when needed
```

---

**Enjoy your new music bot! 🎶**

Made with ❤️ using discord.py and yt-dlp