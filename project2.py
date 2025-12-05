import time
from humanoid import Humanoid
from quarky import Quarky

humanoid = Humanoid(Right_Hip=7, Left_Hip=2, Right_Foot=6, Left_Foot=3, Right_Hand=8, Left_Hand=1)
quarky = Quarky()

SALUTE_ANGLE = 150
NEUTRAL_ANGLE = 90
MARCH_TIME_PERIOD = 800
MARCH_CYCLES = 2

def action_march():
    print("Command: AAGE BADHO (आगे बढ़ो)")
    quarky.showemotion("joy")
    humanoid.move(motion="forward", time_period=MARCH_TIME_PERIOD, cycle=MARCH_CYCLES) 

def action_stop():
    print("Command: RUKO (रुको)")
    quarky.showemotion("cool")
    humanoid.home()
    time.sleep(0.5)

def action_salute():
    print("Command: SALAAMI (सलामी)")
    quarky.displaytext("SALUTE")
    quarky.playsound("victory")

    humanoid.moveall(
        time=500,
        servo_angles=[90, 90, 90, 90, SALUTE_ANGLE, NEUTRAL_ANGLE] 
    )
    time.sleep(1.0)
    
    humanoid.moveall(
        time=500,
        servo_angles=[90, 90, 90, 90, NEUTRAL_ANGLE, NEUTRAL_ANGLE] 
    )
    quarky.stopsound()

def action_turn_right():
    print("Command: DAAYE MUDO (दाएँ मुड़ो)")
    quarky.showemotion("surprised")
    humanoid.move(motion="right", time_period=1000, cycle=1)

def action_display_tiranga():
    print("Command: TIRANGA DIKHAO (तिरंगा दिखाओ)")
    
    S = (255, 100, 0)
    W = (255, 255, 255)
    G = (0, 255, 0)
    B = (0, 0, 255)

    tiranga_matrix = [
        [S, S, S, S, S],
        [S, S, S, S, S],
        [W, W, B, W, W],
        [G, G, G, G, G],
        [G, G, G, G, G]
    ]
    
    quarky.displaymatrix(matrix=tiranga_matrix)
    quarky.displaytext("INDIA")
    time.sleep(3)
    quarky.clear()

def voice_control_loop():
    print("--- Voice Control Mode Initializing (Hindi Commands) ---")
    action_stop()

    while True:
        command = quarky.get_voice_command()
        
        if isinstance(command, str):
            command = command.lower()
        else:
            time.sleep(0.1)
            continue
        
        print(f"Recognized Command: '{command}'")

        if "aage badho" in command or "chalo" in command or "march" in command:
            action_march()
        elif "ruko" in command or "stop" in command or "thehro" in command:
            action_stop()
        elif "salaami" in command or "leharo" in command or "wave" in command:
            action_salute()
        elif "daaye mudo" in command or "dayen mudo" in command or "right" in command:
            action_turn_right()
        elif "tiranga" in command or "flag" in command or "rashtradhwaj" in command:
            action_display_tiranga()
        
        time.sleep(0.1) 

try:
    voice_control_loop()
except Exception as e:
    print(f"Program terminated due to error: {e}")
    humanoid.home()
    quarky.clear()