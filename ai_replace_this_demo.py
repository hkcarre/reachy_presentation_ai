"""
AI Replace This - Presentation Demo Script
============================================
Title: "From 'AI Will Replace Me' to 'AI, Replace This'"

This script provides ready-to-run demo sequences for the Reachy 2 robot.
Run with the Docker simulation for visualization without physical robot.

Setup:
    docker run --rm -p 8888:8888 -p 6080:6080 -p 50051:50051 \
      --name reachy2 docker.io/pollenrobotics/reachy2 \
      start_rviz:=true start_sdk_server:=true fake:=true gazebo:=true

Usage:
    python ai_replace_this_demo.py

Controls:
    1 = Dismissive Handwave (opener)
    2 = Snap to Attention
    3 = Boring Meeting gesture
    4 = Pointing gesture
    5 = Nodding gesture
    6 = Shrug gesture
    7 = Show CURIOUS emotion
    8 = Show DEFEATED emotion
    9 = Show EXCITED emotion
    0 = Show LISTENING emotion
    H = Go to home/default posture
    W = Goodbye wave (closer)
    R = Reset (turn off, go limp)
    Q = Quit

Author: AI Demo Script for Presentation
"""

import logging
import sys
import time
from typing import Optional

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class ReachyDemo:
    """Demo controller for 'AI, Replace This' presentation."""
    
    def __init__(self, host: str = "localhost"):
        """Initialize connection to Reachy robot.
        
        Args:
            host: IP address of the robot or 'localhost' for simulation.
        """
        self.host = host
        self.reachy = None
        self._connect()
    
    def _connect(self) -> bool:
        """Establish connection to the robot."""
        try:
            from reachy2_sdk import ReachySDK
            
            logger.info(f"Connecting to Reachy at {self.host}...")
            self.reachy = ReachySDK(host=self.host)
            
            if self.reachy.is_connected():
                logger.info(f"✅ Connected! Mode: {self.reachy.info.mode}")
                logger.info(f"   Config: {self.reachy.info.config}")
                return True
            else:
                logger.error("❌ Failed to connect to Reachy")
                return False
                
        except Exception as e:
            logger.error(f"❌ Connection error: {e}")
            logger.info("💡 Make sure Docker simulation is running:")
            logger.info("   docker run --rm -p 6080:6080 -p 50051:50051 --name reachy2 docker.io/pollenrobotics/reachy2")
            return False
    
    # =========================================================================
    # ACT 1: THE DISMISSIVE HANDWAVE (Opener)
    # =========================================================================
    
    def slump_defeated(self) -> None:
        """Make robot appear 'defeated' - the starting position.
        
        Presenter says: "Everyone's worried about AI replacing them. But watch this..."
        """
        logger.info("🎭 Slumping into defeated posture...")
        
        if not self.reachy or not self.reachy.is_connected():
            return
            
        # Turn off motors - robot goes limp/compliant
        self.reachy.turn_off()
        time.sleep(0.3)
        
        # If we can still control head while off, droop it
        try:
            if self.reachy.head:
                self.reachy.head.turn_on()
                self.reachy.head.goto([0, -25, 0], duration=1.5)  # Head droops down
                time.sleep(1.5)
                self.reachy.head.turn_off()
        except:
            pass
            
        logger.info("   Robot is now slumped. Ready for the handwave command.")
    
    def snap_to_attention(self) -> None:
        """Snap robot to attention - the power moment.
        
        Presenter waves hand and commands: "AI, stand at attention!"
        """
        logger.info("🎭 Snapping to ATTENTION!")
        
        if not self.reachy or not self.reachy.is_connected():
            return
            
        # Quick turn on
        self.reachy.turn_on()
        time.sleep(0.1)
        
        # Snap to elbow_90 posture (arms forward, ready)
        self.reachy.goto_posture('elbow_90', duration=1.2, wait=False)
        
        # Head looks at presenter
        if self.reachy.head:
            self.reachy.head.look_at(0.5, 0.2, 0.1)  # Look slightly to the side
            
            # Antennas perk up
            try:
                self.reachy.head.l_antenna.goto(15, duration=0.5)
                self.reachy.head.r_antenna.goto(-15, duration=0.5)
            except:
                pass
        
        time.sleep(1.5)
        logger.info("   ✅ Robot at attention. YOU are in command.")
    
    def dismissive_handwave_sequence(self) -> None:
        """Full sequence: slump → pause → snap to attention.
        
        This is the complete opener. Run this before you start talking.
        """
        logger.info("=" * 50)
        logger.info("🎬 ACT 1: THE DISMISSIVE HANDWAVE")
        logger.info("=" * 50)
        
        self.slump_defeated()
        logger.info("   📢 [CUE] Say: 'Everyone's worried about AI replacing them...'")
        time.sleep(3)  # Time for presenter to speak
        
        logger.info("   📢 [CUE] Wave hand and say: 'AI, stand at attention!'")
        time.sleep(1)
        
        self.snap_to_attention()
        logger.info("   📢 [CUE] Say: 'AI doesn't replace you. AI REPORTS to you.'")
    
    # =========================================================================
    # ACT 2: THE LIVE IMPROV DIRECTOR (Main Demo)
    # =========================================================================
    
    def gesture_boring_meeting(self) -> None:
        """Gesture: Reacting to boring meetings.
        
        Head droops (bored) → suddenly perks up → confused antenna twitch.
        Presenter: "AI, replace sitting through boring meetings!"
        """
        logger.info("🎭 Gesture: BORING MEETING reaction")
        
        if not self.reachy or not self.reachy.head:
            return
            
        # Head droops (falling asleep in meeting)
        self.reachy.head.goto([0, -20, 5], duration=1.5)
        time.sleep(1.8)
        
        # Suddenly "wakes up"
        self.reachy.head.goto([0, 10, 0], duration=0.4)
        time.sleep(0.3)
        
        # Confused look - antennas do different things
        try:
            self.reachy.head.l_antenna.goto(25, duration=0.3)
            self.reachy.head.r_antenna.goto(-10, duration=0.3)
        except:
            pass
        
        # Look around confused
        self.reachy.head.goto([10, 5, 15], duration=0.6)
        time.sleep(0.5)
        self.reachy.head.goto([-10, 5, -15], duration=0.6)
        time.sleep(0.5)
        
        # Reset
        self.reachy.head.goto([0, 0, 0], duration=0.5)
        logger.info("   ✅ Even AI finds meetings tedious!")
    
    def gesture_pointing(self) -> None:
        """Gesture: Pointing at the presentation screen.
        
        Presenter: "AI, replace pointing at charts for me!"
        """
        logger.info("🎭 Gesture: POINTING at screen")
        
        if not self.reachy or not self.reachy.r_arm:
            return
            
        # Extend right arm to point
        # Joint order: shoulder_pitch, shoulder_roll, elbow_yaw, elbow_pitch, wrist_roll, wrist_pitch, wrist_yaw
        pointing_pose = [20, 10, -30, -40, 0, -20, 0]
        
        self.reachy.r_arm.goto(pointing_pose, duration=1.2)
        
        # Head looks at where we're pointing
        if self.reachy.head:
            self.reachy.head.goto([0, 5, 30], duration=1.0)
        
        time.sleep(2)
        
        # Small pointing motion (like emphasizing a data point)
        self.reachy.r_arm.goto([25, 10, -30, -40, 0, -20, 0], duration=0.3)
        time.sleep(0.3)
        self.reachy.r_arm.goto([20, 10, -30, -40, 0, -20, 0], duration=0.3)
        
        time.sleep(1)
        
        # Return to neutral
        self.reachy.goto_posture('elbow_90', duration=1.0)
        if self.reachy.head:
            self.reachy.head.goto([0, 0, 0], duration=0.8)
            
        logger.info("   ✅ The classic presenter move - delegated!")
    
    def gesture_nodding(self) -> None:
        """Gesture: Nodding in agreement (the meeting essential).
        
        Presenter: "AI, replace nodding in meetings for me!"
        """
        logger.info("🎭 Gesture: NODDING in agreement")
        
        if not self.reachy or not self.reachy.head:
            return
            
        # Three nods with slight variation
        for i in range(4):
            self.reachy.head.goto([0, 10, 0], duration=0.3)
            time.sleep(0.35)
            self.reachy.head.goto([0, -5, 0], duration=0.25)
            time.sleep(0.3)
        
        # Final knowing look
        self.reachy.head.goto([5, 5, 10], duration=0.5)
        time.sleep(0.5)
        self.reachy.head.goto([0, 0, 0], duration=0.4)
        
        logger.info("   ✅ The most automated action in corporate history!")
    
    def gesture_shrug(self) -> None:
        """Gesture: Shrugging (I don't know / whatever).
        
        Presenter: "Can you even decide to replace me?" 
        Robot shrugs.
        """
        logger.info("🎭 Gesture: SHRUG")
        
        if not self.reachy:
            return
        
        # Both arms up in shrug
        if self.reachy.r_arm:
            self.reachy.r_arm.goto([30, 20, -20, -50, 0, 0, 0], duration=0.6, wait=False)
        if self.reachy.l_arm:
            self.reachy.l_arm.goto([30, -20, 20, -50, 0, 0, 0], duration=0.6, wait=False)
        
        # Head tilts (puzzled)
        if self.reachy.head:
            self.reachy.head.goto([15, 5, 0], duration=0.5)
            try:
                self.reachy.head.l_antenna.goto(20, duration=0.4)
                self.reachy.head.r_antenna.goto(20, duration=0.4)
            except:
                pass
        
        time.sleep(1.5)
        
        # Hold for effect
        time.sleep(1.0)
        
        # Return to neutral
        self.reachy.goto_posture('elbow_90', duration=1.0)
        if self.reachy.head:
            self.reachy.head.goto([0, 0, 0], duration=0.8)
            
        logger.info("   ✅ It can't even want things. YOU are the one with goals.")
    
    def gesture_holding(self) -> None:
        """Gesture: Arms extended, palms up (ready to hold things).
        
        Presenter: "AI, replace holding things for me!"
        """
        logger.info("🎭 Gesture: HOLDING / receiving")
        
        if not self.reachy:
            return
            
        # Extend arms forward with palms up
        if self.reachy.r_arm:
            self.reachy.r_arm.goto([10, -10, 0, -90, 0, 0, 0], duration=1.0, wait=False)
        if self.reachy.l_arm:
            self.reachy.l_arm.goto([10, 10, 0, -90, 0, 0, 0], duration=1.0, wait=False)
            
        if self.reachy.head:
            self.reachy.head.goto([0, -10, 0], duration=0.8)  # Look at hands
        
        time.sleep(2.5)
        
        # Return to neutral
        self.reachy.goto_posture('elbow_90', duration=1.0)
        if self.reachy.head:
            self.reachy.head.goto([0, 0, 0], duration=0.8)
            
        logger.info("   ✅ Basic manipulation - solved!")
    
    # =========================================================================
    # ACT 3: THE EMOTION AMPLIFIER (Closer)
    # =========================================================================
    
    def emotion_curious(self) -> None:
        """Emotion: CURIOUS - head tilts, leans forward, antenna perked.
        
        Presenter: "AI, show me CURIOUS"
        """
        logger.info("🎭 Emotion: CURIOUS")
        
        if not self.reachy or not self.reachy.head:
            return
            
        # Head tilts and looks interested
        self.reachy.head.goto([20, 15, 15], duration=1.0)
        
        # Antennas perk up asymmetrically (curiosity)
        try:
            self.reachy.head.l_antenna.goto(30, duration=0.6)
            self.reachy.head.r_antenna.goto(-5, duration=0.6)
        except:
            pass
        
        time.sleep(2)
        logger.info("   ✅ Curiosity displayed - but only because YOU directed it.")
    
    def emotion_defeated(self) -> None:
        """Emotion: DEFEATED - slumps, looks down.
        
        Presenter: "AI, show me DEFEATED"
        """
        logger.info("🎭 Emotion: DEFEATED")
        
        if not self.reachy:
            return
            
        # Head droops
        if self.reachy.head:
            self.reachy.head.goto([0, -30, 0], duration=1.5)
            try:
                self.reachy.head.l_antenna.goto(-20, duration=1.0)
                self.reachy.head.r_antenna.goto(-20, duration=1.0)
            except:
                pass
        
        # Arms droop slightly
        if self.reachy.r_arm:
            self.reachy.r_arm.goto([5, 5, 0, -100, 0, 0, 0], duration=1.5, wait=False)
        if self.reachy.l_arm:
            self.reachy.l_arm.goto([5, -5, 0, -100, 0, 0, 0], duration=1.5, wait=False)
        
        time.sleep(2)
        logger.info("   ✅ AI can ACT defeated, but it doesn't FEEL defeated.")
    
    def emotion_excited(self) -> None:
        """Emotion: EXCITED - antennas wiggle, arms up, energetic.
        
        Presenter: "AI, show me EXCITED"
        """
        logger.info("🎭 Emotion: EXCITED")
        
        if not self.reachy:
            return
        
        # Quick arm raises
        if self.reachy.r_arm:
            self.reachy.r_arm.goto([40, 30, -20, -60, 0, 0, 0], duration=0.6, wait=False)
        if self.reachy.l_arm:
            self.reachy.l_arm.goto([40, -30, 20, -60, 0, 0, 0], duration=0.6, wait=False)
        
        # Head perks up
        if self.reachy.head:
            self.reachy.head.goto([0, 15, 0], duration=0.5)
            
            # Antenna wiggle!
            try:
                for _ in range(3):
                    self.reachy.head.l_antenna.goto(40, duration=0.15)
                    self.reachy.head.r_antenna.goto(-40, duration=0.15)
                    time.sleep(0.2)
                    self.reachy.head.l_antenna.goto(-20, duration=0.15)
                    self.reachy.head.r_antenna.goto(20, duration=0.15)
                    time.sleep(0.2)
            except:
                pass
        
        time.sleep(1)
        logger.info("   ✅ Excitement performed - because YOU scripted it!")
    
    def emotion_listening(self) -> None:
        """Emotion: LISTENING - tracks speaker, subtle nods.
        
        Presenter: "AI, show me LISTENING"
        """
        logger.info("🎭 Emotion: LISTENING")
        
        if not self.reachy or not self.reachy.head:
            return
            
        # Look at speaker
        self.reachy.head.look_at(0.5, 0.3, 0.1)
        time.sleep(0.5)
        
        # Subtle nods while "listening"
        for _ in range(3):
            self.reachy.head.rotate_by(pitch=5, duration=0.4)
            time.sleep(0.5)
            self.reachy.head.rotate_by(pitch=-5, duration=0.3)
            time.sleep(0.4)
        
        # Slight head tilt (engaged)
        self.reachy.head.rotate_by(roll=8, duration=0.5)
        
        time.sleep(1)
        logger.info("   ✅ Active listening - performed, not felt.")
    
    # =========================================================================
    # CLOSER & UTILITIES
    # =========================================================================
    
    def goodbye_wave(self) -> None:
        """Closing gesture: A friendly wave goodbye.
        
        Presenter: "AI didn't replace me today. It AMPLIFIED me."
        """
        logger.info("🎭 GOODBYE WAVE")
        
        if not self.reachy:
            return
            
        # Raise right arm for wave
        if self.reachy.r_arm:
            self.reachy.r_arm.goto([60, 30, -10, -30, 0, 0, 0], duration=1.0)
            time.sleep(0.5)
            
            # Wave motion
            for _ in range(3):
                self.reachy.r_arm.goto([60, 40, -10, -30, 0, 20, 0], duration=0.3)
                time.sleep(0.35)
                self.reachy.r_arm.goto([60, 20, -10, -30, 0, -20, 0], duration=0.3)
                time.sleep(0.35)
        
        # Head nods goodbye
        if self.reachy.head:
            self.reachy.head.goto([0, 10, 0], duration=0.5)
            time.sleep(0.3)
            self.reachy.head.goto([0, 0, 0], duration=0.3)
        
        time.sleep(1)
        
        # Return to rest
        self.reachy.goto_posture('default', duration=1.5)
        
        logger.info("   ✅ And that's a wrap! AI, standing down.")
    
    def reset(self) -> None:
        """Reset robot to limp/off state."""
        logger.info("🔄 Resetting robot...")
        
        if self.reachy and self.reachy.is_connected():
            self.reachy.turn_off_smoothly()
            
        logger.info("   Robot is now compliant/off.")
    
    def home(self) -> None:
        """Return to home/default posture."""
        logger.info("🏠 Going to home posture...")
        
        if not self.reachy:
            return
            
        self.reachy.turn_on()
        self.reachy.goto_posture('default', duration=2.0, wait=True)
        
        if self.reachy.head:
            self.reachy.head.goto([0, 0, 0], duration=1.0)
            
        logger.info("   ✅ Home position.")
    
    def disconnect(self) -> None:
        """Clean disconnect from robot."""
        if self.reachy:
            self.reset()
            self.reachy.disconnect()
            logger.info("👋 Disconnected from Reachy.")


def print_controls():
    """Print the control guide."""
    print("\n" + "=" * 60)
    print("  'AI, Replace This' - DEMO CONTROLS")
    print("=" * 60)
    print("""
  ACT 1: THE OPENER
    1 = Full Handwave Sequence (slump → attention)
    2 = Snap to Attention only
    
  ACT 2: IMPROV DIRECTOR GESTURES  
    3 = Boring Meeting reaction
    4 = Pointing at screen
    5 = Nodding in agreement
    6 = Shrug (I don't know)
    
  ACT 3: EMOTION AMPLIFIER
    7 = CURIOUS emotion
    8 = DEFEATED emotion
    9 = EXCITED emotion
    0 = LISTENING emotion
    
  UTILITIES
    H = Home/default posture
    W = Goodbye Wave (closer)
    R = Reset (turn off)
    Q = Quit demo
    """)
    print("=" * 60 + "\n")


def main():
    """Main demo loop with keyboard controls."""
    print("\n" + "🤖" * 30)
    print("\n  FROM 'AI WILL REPLACE ME' TO 'AI, REPLACE THIS'")
    print("  Reachy 2 Robot Demo Script")
    print("\n" + "🤖" * 30)
    
    # Initialize demo
    demo = ReachyDemo(host="localhost")
    
    if not demo.reachy or not demo.reachy.is_connected():
        print("\n❌ Could not connect to robot. Exiting.")
        sys.exit(1)
    
    print_controls()
    
    # Start in attention position
    print("📍 Starting in default position...")
    demo.home()
    
    # Main control loop
    try:
        while True:
            key = input("\n🎮 Enter command (or 'Q' to quit): ").strip().upper()
            
            if key == '1':
                demo.dismissive_handwave_sequence()
            elif key == '2':
                demo.snap_to_attention()
            elif key == '3':
                demo.gesture_boring_meeting()
            elif key == '4':
                demo.gesture_pointing()
            elif key == '5':
                demo.gesture_nodding()
            elif key == '6':
                demo.gesture_shrug()
            elif key == '7':
                demo.emotion_curious()
            elif key == '8':
                demo.emotion_defeated()
            elif key == '9':
                demo.emotion_excited()
            elif key == '0':
                demo.emotion_listening()
            elif key == 'H':
                demo.home()
            elif key == 'W':
                demo.goodbye_wave()
            elif key == 'R':
                demo.reset()
            elif key == 'Q':
                print("\n👋 Ending demo...")
                break
            else:
                print("   ⚠️ Unknown command. Press H for help or Q to quit.")
                print_controls()
                
    except KeyboardInterrupt:
        print("\n\n⚠️ Interrupted by user.")
    finally:
        demo.disconnect()
        print("\n✅ Demo ended. Thanks for presenting!")


if __name__ == "__main__":
    main()
