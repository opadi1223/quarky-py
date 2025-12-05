import time
from quarky import *

quarky = Quarky() 
quarky.setorientation("HORIZONTAL")

def control_quarky_by_gesture():
    print("Starting Hand Gesture Control loop...")

    movement_speed = 60 

    while True:
        current_gesture = quarky.get_ml_result("Hand Pose")
        
        if current_gesture == "Left_Hand":
            quarky.runrobot("LEFT", movement_speed)
            print("Action: Moving Left")
        
        elif current_gesture == "Right_Hand":
            quarky.runrobot("RIGHT", movement_speed)
            print("Action: Moving Right")
            
        else:
            quarky.stoprobot()
            
        time.sleep(0.1) 

if __name__ == "__main__":
    try:
        control_quarky_by_gesture()
    except KeyboardInterrupt:
        quarky.stoprobot()
        print("\nProgram stopped. Robot halted.")