#!/usr/bin/env python3
"""
Test script to verify the music bot imports correctly and dependencies are installed.
Run this before starting your bot!
"""

import sys

def test_imports():
    """Test if all required modules can be imported"""
    print("🔍 Testing imports...")
    
    try:
        import discord
        print(f"✅ discord.py {discord.__version__}")
    except ImportError as e:
        print(f"❌ discord.py not found: {e}")
        return False
    
    try:
        import yt_dlp
        print(f"✅ yt-dlp")
    except ImportError as e:
        print(f"❌ yt-dlp not found: {e}")
        return False
    
    try:
        from discord.ext import commands, tasks
        print("✅ discord.ext.commands and tasks")
    except ImportError as e:
        print(f"❌ discord.ext imports failed: {e}")
        return False
    
    try:
        import asyncio
        print("✅ asyncio")
    except ImportError as e:
        print(f"❌ asyncio not found: {e}")
        return False
    
    try:
        import os
        print("✅ os")
    except ImportError as e:
        print(f"❌ os not found: {e}")
        return False
    
    return True

def check_ffmpeg():
    """Check if FFmpeg is installed"""
    print("\n🎵 Checking FFmpeg...")
    
    import subprocess
    try:
        result = subprocess.run(['ffmpeg', '-version'], 
                              capture_output=True, 
                              text=True,
                              timeout=5)
        if result.returncode == 0:
            version_line = result.stdout.split('\n')[0]
            print(f"✅ FFmpeg is installed: {version_line}")
            return True
        else:
            print("❌ FFmpeg not found or not in PATH")
            print("   Install FFmpeg from: https://ffmpeg.org/download.html")
            return False
    except FileNotFoundError:
        print("❌ FFmpeg not found in system PATH")
        print("   Install FFmpeg and add to PATH environment variable")
        return False
    except subprocess.TimeoutExpired:
        print("⚠️  FFmpeg check timed out (might be slow)")
        return True

def test_bot_import():
    """Test if the bot module can be imported"""
    print("\n🤖 Testing bot module...")
    
    try:
        import music_bot
        print("✅ music_bot.py imported successfully")
        return True
    except Exception as e:
        print(f"❌ Failed to import music_bot: {e}")
        return False

def check_files():
    """Check if all necessary files exist"""
    print("\n📁 Checking required files...")
    
    import os
    
    files = [
        'music_bot.py',
        'requirements.txt',
        'README.md'
    ]
    
    for file in files:
        if os.path.exists(file):
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} not found!")
            return False
    
    return True

def main():
    """Run all tests"""
    print("=" * 60)
    print("🎵 Discord Music Bot - Pre-flight Check")
    print("=" * 60)
    
    all_passed = True
    
    # Test imports
    if not test_imports():
        all_passed = False
        print("\n❌ Some dependencies are missing!")
        print("   Run: pip install -r requirements.txt")
    
    # Check FFmpeg
    ffmpeg_ok = check_ffmpeg()
    if not ffmpeg_ok:
        all_passed = False
    
    # Test bot import
    if not test_bot_import():
        all_passed = False
    
    # Check files
    if not check_files():
        all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("✅ All checks passed! You're ready to run the bot.")
        print("   Run: python music_bot.py")
    else:
        print("❌ Some checks failed. Please fix the issues above.")
    print("=" * 60)
    
    return all_passed

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)