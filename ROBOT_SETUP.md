# Robot Setup Guide

## How to Make the Robot Work in the Presentation

The presentation embeds a live view of the Reachy 2 robot simulation. Here's how to set it up:

---

## Quick Start (3 Steps)

### Step 1: Start the Robot Simulation

Open **PowerShell** or **Terminal** and run:

```bash
docker run --rm -p 8888:8888 -p 6080:6080 -p 50051:50051 --name reachy2 docker.io/pollenrobotics/reachy2 start_rviz:=true start_sdk_server:=true fake:=true gazebo:=true
```

Wait about 30-60 seconds for the simulation to fully initialize.

### Step 2: Verify the Robot is Running

Open your browser and go to:

```
http://localhost:6080/vnc.html?autoconnect=1&resize=remote
```

You should see the Reachy robot in a 3D visualization (RViz/Gazebo).

### Step 3: Run the Demo Controller

In a **new terminal window**:

```bash
cd c:\Dev\AI_presentation\reachy2-sdk-develop\presentation
python ai_replace_this_demo.py
```

Now you can use keyboard controls:
- **1** = Opener sequence (slump → attention)
- **3-6** = Gestures
- **7-0** = Emotions
- **W** = Wave goodbye

---

## Presentation Setup

### Option A: Presentation + Separate Robot Window (Recommended)

1. Open the presentation: `http://localhost:8080`
2. Open robot viewer in a separate window: `http://localhost:6080`
3. Arrange windows side by side on your display

### Option B: Embedded Robot in Presentation

The presentation already embeds the robot view. Just:
1. Start Docker simulation (Step 1 above)
2. Open the presentation: `http://localhost:8080`
3. The robot frames will show the live simulation automatically

---

## Requirements

- **Docker Desktop** - [Download here](https://www.docker.com/products/docker-desktop/)
- **Python 3.10+** - [Download here](https://www.python.org/downloads/)
- **reachy2-sdk** - Install with: `pip install reachy2-sdk`

---

## Troubleshooting

### Robot frame shows blank/error
- Make sure Docker simulation is running (Step 1)
- Wait 30-60 seconds after starting Docker
- Refresh the presentation page

### Cannot connect to robot
- Check that ports 6080 and 50051 are not used by other apps
- Try restarting Docker Desktop

### Robot not responding to controls
- Make sure `ai_replace_this_demo.py` is running
- Check that the script shows "Connected" status
- Press `H` to reset robot to home position

---

## Presentation Day Checklist

- [ ] Docker Desktop installed and running
- [ ] Start robot simulation 5 minutes before presentation
- [ ] Test robot visualization loads in browser
- [ ] Run demo script and test controls
- [ ] Position windows (presentation + robot view)
- [ ] Have backup: pre-recorded video of robot movements

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        YOUR LAPTOP                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────┐    ┌─────────────────────────────────┐│
│  │  Docker         │    │  Python Demo Script             ││
│  │  Container      │    │  ai_replace_this_demo.py        ││
│  │                 │    │                                 ││
│  │  - Gazebo Sim   │◄───│  Sends commands via gRPC        ││
│  │  - RViz         │    │  (port 50051)                   ││
│  │  - SDK Server   │    │                                 ││
│  └────────┬────────┘    └─────────────────────────────────┘│
│           │                                                 │
│           │ VNC (port 6080)                                 │
│           ▼                                                 │
│  ┌─────────────────────────────────────────────────────────┐│
│  │  Browser                                                ││
│  │  - Presentation (index.html)                            ││
│  │  - Embedded robot iframe ← VNC stream                   ││
│  └─────────────────────────────────────────────────────────┘│
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Demo Flow

1. **Before you start talking**: Press `1` (robot slumps)
2. **"AI, stand at attention"**: Press `2` (robot snaps up)
3. **Audience interaction**: Press `3-6` for gestures
4. **Emotion demo**: Press `7-0` for emotions
5. **Goodbye**: Press `W` for wave
