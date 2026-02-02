# AI, Replace This - Presentation Package

**"From 'AI Will Replace Me' to 'AI, Replace This'"**

A live robot demonstration for AI audiences using Pollen Robotics Reachy 2.

## 🚀 Quick Start

### 1. Start the Robot Simulation

```bash
docker run --rm -p 8888:8888 -p 6080:6080 -p 50051:50051 \
  --name reachy2 docker.io/pollenrobotics/reachy2 \
  start_rviz:=true start_sdk_server:=true fake:=true gazebo:=true
```

### 2. Open the Presentation

Open `index.html` in your browser, or serve it locally:

```bash
# Using Python
python -m http.server 8000

# Then open: http://localhost:8000
```

### 3. Run the Demo Script

In a separate terminal:

```bash
pip install reachy2-sdk
python ai_replace_this_demo.py
```

## 📁 Files

| File | Description |
|------|-------------|
| `index.html` | Main presentation (Reveal.js slides) |
| `demo.html` | Live robot visualization + controls reference |
| `ai_replace_this_demo.py` | Python script to control the robot |

## 🎬 Presentation Flow

### Act 1: The Opener (30 sec)
- Robot slumped → snaps to attention
- Key: `1`
- Punchline: "AI doesn't replace you. AI REPORTS to you."

### Act 2: Live Improv Director (3-4 min)
- Audience requests tasks to "replace"
- Keys: `3` (bored) `4` (point) `5` (nod) `6` (shrug)
- Frame: "AI, Replace THIS!"

### Act 3: Emotion Amplifier (1-2 min)
- Show AI performing emotions on command
- Keys: `7` (curious) `8` (defeated) `9` (excited) `0` (listening)
- Punchline: "AI is a blank canvas. YOU bring the intent."

### Closer
- Key: `W` for goodbye wave
- "AI didn't replace me today. It AMPLIFIED me."

## ⌨️ Keyboard Controls

| Key | Action |
|-----|--------|
| 1 | Full opener sequence |
| 2 | Snap to attention |
| 3 | Boring meeting reaction |
| 4 | Pointing gesture |
| 5 | Nodding |
| 6 | Shrug |
| 7 | Show CURIOUS |
| 8 | Show DEFEATED |
| 9 | Show EXCITED |
| 0 | Show LISTENING |
| H | Home position |
| W | Goodbye wave |
| R | Reset (turn off) |
| Q | Quit demo |

## 🌐 GitHub Pages Deployment

This repository is configured for GitHub Pages. After pushing:

1. Go to repository Settings → Pages
2. Select source: "Deploy from a branch"
3. Select branch: `main` and folder `/ (root)`
4. Your presentation will be at: `https://hkcarre.github.io/reachy_presentation_ai/`

## 📚 Resources

- [Reachy 2 SDK Documentation](https://pollen-robotics.github.io/reachy2-sdk/reachy2_sdk.html)
- [Pollen Robotics](https://www.pollen-robotics.com/)
- [Docker Hub - Reachy 2](https://hub.docker.com/r/pollenrobotics/reachy2)

## 📝 License

MIT License - Created for educational/presentation purposes.
