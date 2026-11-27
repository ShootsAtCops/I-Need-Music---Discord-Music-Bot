# 🚀 Installation Guide

## Complete Step-by-Step Instructions

### Prerequisites Checklist
- [ ] Python 3.8 or higher installed
- [ ] FFmpeg installed on your system
- [ ] Discord account created
- [ ] Discord Developer Portal access
- [ ] Git (optional, for version control)

---

## Step 1: Install Python (if needed)

### Windows
1. Download Python from: https://www.python.org/downloads/
2. Run the installer
3. ✅ **Important:** Check "Add Python to PATH" during installation
4. Verify: Open Command Prompt and run `python --version`

### macOS
```bash
# Using Homebrew (recommended)
brew install python

# Or from python.org
# Download and run the .pkg file
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3.8 python3.8-venv python3-pip
```

### Verify Python Installation
```bash
python --version
# Should show: Python 3.8.x or higher
```

---

## Step 2: Install FFmpeg

FFmpeg is required for audio processing.

### Windows
**Option A - Official Website:**
1. Download from: https://ffmpeg.org/download.html
2. Extract the ZIP file
3. Add `bin` folder to PATH:
   - Right-click "This PC" → Properties → Advanced System Settings
   - Click "Environment Variables"
   - Under "System variables", select "Path" → Edit → New
   - Add: `C:\path\to\ffmpeg\bin`
   - Click OK

**Option B - Chocolatey (if installed):**
```bash
choco install ffmpeg
```

**Option C - Scoop:**
```bash
scoop install ffmpeg
```

### macOS
```bash
# Using Homebrew
brew install ffmpeg

# Verify
ffmpeg -version
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install ffmpeg

# Verify
ffmpeg -version
```

### Linux (Fedora/CentOS)
```bash
sudo yum install ffmpeg
```

### Verify FFmpeg Installation
```bash
ffmpeg -version
# Should show FFmpeg version info
```

---

## Step 3: Create Discord Bot

1. **Go to Discord Developer Portal:**
   https://discord.com/developers/applications

2. **Create New Application:**
   - Click "New Application"
   - Enter a name (e.g., "Music Bot")
   - Click "Create"

3. **Create the Bot:**
   - In the left sidebar, click "Bot"
   - Click "Add Bot" → "Yes, do it!"

4. **Get Your Token:**
   - Under "Token", click "Copy"
   - ⚠️ **Save this token securely!** You'll need it for `music_bot.py`
   - Click "Reset Token" if you want a new one

5. **Enable Required Permissions:**
   - Still in the Bot section, scroll down to "Privileged Gateway Intents"
   - Enable:
     - ✅ **MESSAGE CONTENT INTENT**
     - ✅ **SERVER MEMBERS INTENT** (optional but recommended)

6. **Invite Bot to Your Server:**
   - Go to "OAuth2" → "URL Generator" in left sidebar
   - Select scopes: `bot` and `applications.commands`
   - Select bot permissions:
     - ✅ Read Messages/View Channels
     - ✅ Send Messages
     - ✅ Connect
     - ✅ Speak
   - Copy the generated URL
   - Open URL in browser and select your server
   - Click "Authorize"

---

## Step 4: Set Up Project

### Option A: Using Existing Files
If you already have the files from the main repository:
```bash
cd music-bot-folder
```

### Option B: Clone Repository (Recommended)
```bash
git clone https://github.com/ShootsAtCops/music-bot.git
cd music-bot
```

---

## Step 5: Install Python Dependencies

### Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

### Install Requirements
```bash
pip install -r requirements.txt
```

This will install:
- discord.py (Discord API library)
- yt-dlp (Music extraction from various sources)
- ffmpeg-python (Audio processing)

### Verify Installation
```bash
python -c "import discord; import yt_dlp; print('✅ All dependencies installed!')"
```

---

## Step 6: Configure the Bot

1. **Open `music_bot.py` in a text editor**

2. **Find this line:**
   ```python
   TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
   ```

3. **Replace with your token:**
   ```python
   TOKEN = 'your-actual-bot-token-here'
   ```

4. **Save the file**

5. **Optional: Create a `.env` file** (more secure)
   ```
   DISCORD_TOKEN=your-actual-bot-token-here
   ```
   
   Then modify `music_bot.py` to use:
   ```python
   import os
   from dotenv import load_dotenv
   
   load_dotenv()
   TOKEN = os.getenv('DISCORD_TOKEN')
   ```

---

## Step 7: Download Cookies (Optional but Recommended)

Cookies help the bot play age-restricted or region-locked videos.

### How to Get Cookies:

1. **Install Extension:**
   - Chrome: [Get cookies.txt](https://chrome.google.com/webstore/detail/get-cookiestxt/oknfoidjnjfofmieeigfakfgkkkeffeb)
   - Firefox: [cookies.txt Export](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt-export/)

2. **Export Cookies:**
   - Go to YouTube.com
   - Log in with your Google account (optional but recommended)
   - Click the extension icon
   - Select "YouTube" domain
   - Click "Export Selected Cookie Jar"
   - Save as `cookies.txt`

3. **Place File:**
   - Put `cookies.txt` in the same folder as `music_bot.py`
   - The bot will automatically detect it

---

## Step 8: Test Before Running Bot

Run the test script to verify everything is set up correctly:

```bash
python test_bot.py
```

Expected output:
```
============================================================
🎵 Discord Music Bot - Pre-flight Check
============================================================
🔍 Testing imports...
✅ discord.py 2.3.2
✅ yt-dlp
✅ discord.ext.commands and tasks
✅ asyncio
✅ os

🎵 Checking FFmpeg...
✅ FFmpeg is installed: ffmpeg version 5.x.x

🤖 Testing bot module...
✅ music_bot.py imported successfully

📁 Checking required files...
✅ music_bot.py exists
✅ requirements.txt exists
✅ README.md exists

============================================================
✅ All checks passed! You're ready to run the bot.
   Run: python music_bot.py
============================================================
```

If any checks fail, fix the issues before proceeding.

---

## Step 9: Run the Bot

```bash
python music_bot.py
```

Expected output:
```
2026-11-25 10:30:45 - INFO - Logged in as MusicBot#1234 (ID: 123456789)
2026-11-25 10:30:45 - INFO - Discord API version: 2.0
```

The bot is now running! Check your Discord server to see it.

---

## Step 10: Use the Bot

### In Discord:
1. Make sure the bot is in a voice channel with you
2. Type commands like:
   ```
   \play Linkin Park - Numb
   \queue
   \insert https://youtube.com/watch?v=example
   \clear
   ```

---

## Common Installation Issues

### Issue: "No module named 'discord'"
**Solution:**
```bash
pip install discord.py
```

### Issue: "No module named 'yt_dlp'"
**Solution:**
```bash
pip install yt-dlp
```

### Issue: "FFmpeg not found" or "ffmpeg: command not found"
**Solution:**
- Make sure FFmpeg is installed (Step 2)
- Add FFmpeg to your system PATH
- Verify with: `ffmpeg -version`

### Issue: "The bot token is invalid"
**Solution:**
- Double-check you copied the correct token
- Make sure there are no spaces or extra characters
- Try getting a new token from Discord Developer Portal

### Issue: Bot doesn't respond to commands
**Solutions:**
1. Check that bot has proper permissions in server settings
2. Verify "MESSAGE CONTENT INTENT" is enabled
3. Make sure you're using slash commands (`\play` not `!play`)
4. Check console for error messages

### Issue: Can't play certain videos
**Solutions:**
1. Try downloading and using `cookies.txt`
2. Some videos may be region-locked or age-restricted
3. Check if the URL format is correct

---

## Running as a Service (Optional)

### Windows - Use Task Scheduler
1. Open Task Scheduler
2. Create Basic Task
3. Set trigger (e.g., when computer starts)
4. Action: Start a program
   - Program: `python.exe`
   - Arguments: `path\to\music_bot.py`
   - Start in: `path\to\folder`

### macOS - Use launchd
Create file: `~/Library/LaunchAgents/com.yourname.musicbot.plist`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.yourname.musicbot</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/Users/yourname/music_bot.py</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
```
Load with: `launchctl load ~/Library/LaunchAgents/com.yourname.musicbot.plist`

### Linux - Use systemd
Create file: `/etc/systemd/system/musicbot.service`
```ini
[Unit]
Description=Discord Music Bot
After=network.target

[Service]
Type=simple
User=ShootsAtCops
WorkingDirectory=/path/to/music-bot
ExecStart=/usr/bin/python3 /path/to/music_bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```
Enable with: `systemctl enable musicbot.service`

---

## Next Steps

1. ✅ Run the test script: `python test_bot.py`
2. ✅ Start the bot: `python music_bot.py`
3. ✅ Invite bot to your server (if not already done)
4. ✅ Test with `\play` command
5. ✅ Explore all features!

---

## Need Help?

- **Documentation:** See README.md for full feature list
- **Examples:** Check USAGE_EXAMPLES.md for usage guide
- **Troubleshooting:** Refer to main README.md troubleshooting section
- **yt-dlp support sites:** https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md

---

**Happy Music Playing! 🎵**