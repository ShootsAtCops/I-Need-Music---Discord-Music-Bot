# ⚡ Quick Start Guide

## Get Your Bot Running in 3 Minutes!

### Step 1: Install (1 minute)
```bash
# Create virtual environment and install
cd music-bot-folder
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Step 2: Get Token (1 minute)
1. Go to https://discord.com/developers/applications
2. Create new application → Add bot → Copy token
3. Enable "MESSAGE CONTENT INTENT"

### Step 3: Configure & Run (1 minute)
```bash
# Edit the file
code music_bot.py  # or use your preferred editor

# Replace line 150:
TOKEN = 'your-actual-token-here'

# Test setup
python test_bot.py

# If all ✅, run the bot!
python music_bot.py
```

---

## In Discord - Start Using Immediately

### 1. Invite Bot to Server
Use this URL (replace TOKEN):
```
https://discord.com/api/oauth2/authorize?client_id=TOKEN&permissions=8&scope=bot%20applications.commands
```

### 2. Join Voice Channel with Bot
You and the bot must be in the same voice channel.

### 3. Try Commands
```bash
# Play a song (it will start immediately)
play Linkin Park - Numb

# Add more songs to queue
play Eminem - Lose Yourself
play Imagine Dragons - Believer

# See the queue
queue

# Insert a favorite at the TOP of queue
insert https://youtube.com/watch?v=your-video-id

# Clear everything and start fresh
ear

# Skip current song
skip

# Stop all music
stop
```

---

## That's It! 🎉

Your bot is now running with:
- ✅ Play any song from URL
- ✅ Queue system for multiple songs
- ✅ Insert at top of queue
- ✅ Clear all queue function

---

## Need Help?

- **Full installation:** See `INSTALLATION_GUIDE.md`
- **Usage examples:** See `USAGE_EXAMPLES.md`
- **Queue system:** See `QUEUE_SYSTEM_GUIDE.md`
- **All features:** See `README.md`

---

## Common First-Time Issues

**Issue:** "Module not found"
```bash
pip install discord.py yt-dlp
```

**Issue:** "FFmpeg not found"
- Install FFmpeg: https://ffmpeg.org/download.html
- Add to PATH environment variable

**Issue:** Can't play certain videos
- Download cookies.txt (optional but recommended)
- See `INSTALLATION_GUIDE.md` for instructions

---

## Next Steps After Running

1. ✅ Test with a simple YouTube URL
2. ✅ Try adding songs to queue
3. ✅ Test `insert` command
4. ✅ Clear and rebuild queue
5. ✅ Explore all supported sources!

**Happy Music Playing! 🎵**