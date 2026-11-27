# 📊 Queue System Visual Guide

## How the Music Queue Works

### Visual Representation

```
┌─────────────────────────────────────────────────────────────┐
│                    DISCORD MUSIC BOT                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Voice Channel: #music                                      │
│  ┌──────────────────────────────────────────────────┐      │
│  │ Bot Connected                                    │      │
│  └──────────────────────────────────────────────────┘      │
│                                                             │
│  🎵 Currently Playing:                                      │
│     Linkin Park - Numb (04:38)                             │
│                                                             │
│  📋 Queue (2 songs):                                        │
│     1. Eminem - Lose Yourself (03:49)                      │
│     2. Imagine Dragons - Believer (03:14)                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Command Flow Diagrams

### 1. Playing a Song (play)

```
User types: play Linkin Park - Numb
        ↓
Bot checks: Is bot in voice channel? ✅
        ↓
Bot checks: Is song already playing?
    ├─ NO → Play immediately, add to queue[0]
    └─ YES → Add to end of queue, skip current message
        ↓
Song downloads via yt-dlp
        ↓
Audio streams to voice channel
        ↓
User sees: "Now Playing: Linkin Park - Numb"
```

### 2. Adding to Queue (when song is playing)

```
Current State:
┌─────────────────────────────────┐
│ 🎵 Playing: Song A              │
│ 📋 Queue: [Song B, Song C]      │
└─────────────────────────────────┘
        ↓
User types: play Song D
        ↓
Bot adds to END of queue
        ↓
New State:
┌─────────────────────────────────┐
│ 🎵 Playing: Song A              │
│ 📋 Queue: [Song B, Song C, Song D]  │
└─────────────────────────────────┘
```

### 3. Inserting at Top (insert)

```
Current State:
┌─────────────────────────────────┐
│ 🎵 Playing: Song A              │
│ 📋 Queue: [Song B, Song C]      │
└─────────────────────────────────┘
        ↓
User types: insert Song D
        ↓
Bot inserts at POSITION 0 (top)
        ↓
New State:
┌─────────────────────────────────┐
│ 🎵 Playing: Song A              │
│ 📋 Queue: [Song D, Song B, Song C]  │
└─────────────────────────────────┘

Note: Song D will play BEFORE Song B and C
```

### 4. Skipping (skip)

```
Current State:
┌─────────────────────────────────┐
│ 🎵 Playing: Song A              │
│ 📋 Queue: [Song B, Song C]      │
└─────────────────────────────────┘
        ↓
User types: skip
        ↓
Current song stops immediately
        ↓
Next song in queue starts playing
        ↓
New State:
┌─────────────────────────────────┐
│ 🎵 Playing: Song B              │
│ 📋 Queue: [Song C]              │
└─────────────────────────────────┘
```

### 5. Clearing Queue (ear)

```
Current State:
┌─────────────────────────────────┐
│ 🎵 Playing: Song A              │
│ 📋 Queue: [Song B, Song C]      │
└─────────────────────────────────┘
        ↓
User types: ear
        ↓
All songs removed from queue
Current playing cleared too
        ↓
New State:
┌─────────────────────────────────┐
│ 🎵 Playing: None                │
│ 📋 Queue: []                    │
└─────────────────────────────────┘
```

---

## Example Scenario Walkthrough

### Initial State
```
User joins voice channel with bot
Bot is not playing anything
Queue is empty
```

### Step 1: First Song
```
User: play Song A
Result:
┌─────────────────────────────────┐
│ 🎵 Playing: Song A              │
│ 📋 Queue: []                    │
└─────────────────────────────────┘
```

### Step 2: Add More Songs
```
User: play Song B
User: play Song C
Result:
┌─────────────────────────────────┐
│ 🎵 Playing: Song A              │
│ 📋 Queue: [Song B, Song C]      │
└─────────────────────────────────┘
```

### Step 3: Insert Favorite
```
User: insert Song D (their favorite!)
Result:
┌─────────────────────────────────┐
│ 🎵 Playing: Song A              │
│ 📋 Queue: [Song D, Song B, Song C]  │
└─────────────────────────────────┘
```

### Step 4: Skip Current
```
User: skip (hates current song)
Result:
┌─────────────────────────────────┐
│ 🎵 Playing: Song D              │
│ 📋 Queue: [Song B, Song C]      │
└─────────────────────────────────┘
```

### Step 5: Clear Everything
```
User: ear (starting fresh)
Result:
┌─────────────────────────────────┐
│ 🎵 Playing: None                │
│ 📋 Queue: []                    │
└─────────────────────────────────┘
```

---

## Queue Index Positions

```
Position 0 (Top):    [Song inserted with insert]
Position 1:          [First queued song]
Position 2:          [Second queued song]
Position 3:          [Third queued song]
...
Position N:          [Last in queue]

Currently Playing:   [Separate from queue, plays first]
```

---

## Queue Management Commands

| Command | Effect on Queue | Example |
|---------|----------------|---------|
| `play` | Adds to END if song playing | Current: A → Queue: [B] |
| `insert` | Adds to TOP (position 0) | Current: A, Q:[B,C] → Q:[D,B,C] |
| `skip` | Removes current, plays next in queue | Current: A, Q:[B] → Current: B, Q:[] |
| `ear` | Empties entire queue + current | All cleared |

---

## Advanced Queue Scenarios

### Scenario 1: Building a Playlist
```
User wants to play: Song A → Song B → Song C

Step 1:
play Song A
Result: Playing A, Queue: []

Step 2:
play Song B
Result: Playing A, Queue: [B]

Step 3:
play Song C
Result: Playing A, Queue: [B, C]

Step 4 (when A finishes):
Playing B, Queue: [C]

Step 5:
Playing C, Queue: []
```

### Scenario 2: Emergency Insertion
```
User is playing a playlist but wants to add a favorite NOW

Current State:
Playing: Playlist Song 5
Queue: [Song 6, Song 7, ...]

Action:
insert My Favorite Song

New State:
Playing: Playlist Song 5
Queue: [My Favorite Song, Song 6, Song 7, ...]

Result: When song 5 ends, favorite plays immediately!
```

### Scenario 3: Clear and Restart
```
User wants to start fresh after a long session

Current State:
Playing: Song X
Queue: [Y, Z, W] (10 hours of music)

Action:
ear

New State:
Playing: None
Queue: []

Result: Clean slate to build new playlist
```

---

## Queue Display Examples

### Empty Queue
```
📭 **Queue is empty!**
```

### Single Song in Queue
```
🎵 Currently Playing: Song A (05:30)

📋 Queue (1 song):

1. **Song B**
⏱️ 04:15
```

### Multiple Songs in Queue
```
🎵 Currently Playing: Song A (05:30)

📋 Queue (5 songs):

1. **Eminem - Lose Yourself**
⏱️ 03:49

2. **Imagine Dragons - Believer**
⏱️ 03:14

3. **Linkin Park - Numb**
⏱️ 04:38

4. **OneRepublic - Counting Stars**
⏱️ 04:21

5. **The Weeknd - Blinding Lights**
⏱️ 03:49
```

---

## Tips for Effective Queue Management

### ✅ Do:
- Use `insert` when you want a song to play sooner
- Check `queue` before using `ear` to see what you're losing
- Add songs while music is playing (they auto-queue)
- Use `/nowplaying` to see current song details

### ❌ Don't:
- Use `ear` accidentally (can't undo!)
- Expect `insert` to play immediately (it goes in queue first)
- Assume queue order is preserved after `skip` (current changes)
- Try to add songs when bot isn't in voice channel

---

## Queue Limits

- **Maximum queue size:** Limited by Discord's message length (~2000 characters)
- **Practical limit:** ~50-100 songs depending on titles and durations
- **Storage:** Songs are downloaded temporarily, not permanently stored
- **Memory:** Queue data is kept in RAM while bot is running

---

**Understanding the queue system makes you a better music bot user! 🎵**