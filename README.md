1. Code Explanation (quarky_gesture_control.py)
This Python script is designed to be the core logic for controlling a Quarky robot using real-time hand gesture recognition.

Section	Code	Purpose
Setup	
import time


from quarky import *


quarky = Quarky()


quarky.setorientation("HORIZONTAL")

Imports necessary libraries (time for pauses, quarky for hardware control). Initializes the Quarky object and sets the robot's orientation, which is crucial for the robot to understand "Left" and "Right" directions correctly.
Main Function	def control_quarky_by_gesture():	Defines the main loop that handles gesture detection and robot movement.
Speed Setup	movement_speed = 60	Sets the speed for the motors. This value can range from 0 (stopped) to 100 (maximum speed).
Control Loop	while True:	This creates an infinite loop, ensuring the robot continuously checks for gestures until the program is manually stopped.
Gesture Input	current_gesture = quarky.get_ml_result("Hand Pose")	This is the most crucial line. It calls a function specific to the PictoBlox/Quarky library to fetch the currently recognized class from the running Machine Learning model (which is expected to be a Hand Pose Classifier).
Logic (Left)	
if current_gesture == "Left_Hand":


quarky.runrobot("LEFT", movement_speed)


print("Action: Moving Left")

If the ML model recognizes the output class "Left_Hand", the robot runs its motors to move in the LEFT direction at the specified speed.
Logic (Right)	
elif current_gesture == "Right_Hand":


quarky.runrobot("RIGHT", movement_speed)


print("Action: Moving Right")

If the ML model recognizes the output class "Right_Hand", the robot runs its motors to move in the RIGHT direction.
Logic (Stop)	
else:


quarky.stoprobot()

If the recognized class is anything else (e.g., "None," "Background," or an unclassified pose), the robot stops immediately.
Timing	time.sleep(0.1)	Pauses the loop for 0.1 seconds. This prevents the code from running too fast, which can consume too much power and prevent reliable detection.
Execution	
if __name__ == "__main__":


try: ... except KeyboardInterrupt: ...

Standard Python structure to run the main function and ensure the robot stops gracefully if the user manually stops the script (e.g., by pressing Ctrl+C).

Export to Sheets

2. Hardware and Setup
To execute this program, you need:

Quarky Board: The main microcontroller board.

Quarky Robot/Chassis: The physical robot base with wheels and motors connected to the Quarky board. (The code uses quarky.runrobot, implying a completed robot build).

Power Supply: The robot must be built and powered on.

Computer/Laptop: Running the PictoBlox software.

Webcam: To capture the user's hand gestures so the ML model can analyze them.

3. How to Execute This in PictoBlox
This code is written for Python Mode within the PictoBlox software environment and relies on a previously trained Machine Learning model.

Step 1: Train the ML Model (Prerequisite)
Before running the code, you must first create and train a Hand Pose Classifier model in PictoBlox:

Create Model: Open the Machine Learning extension in PictoBlox and select "Hand Pose Classifier."

Collect Data: Create at least two classes, exactly named "Left_Hand" and "Right_Hand". Collect several samples of your hand in the appropriate position for each class using your webcam.

Train & Export: Train the model. Once trained, you must export or deploy the model so that the PictoBlox environment knows which model to use when the Python code calls quarky.get_ml_result("Hand Pose").

Step 2: Switch to Python Mode
In PictoBlox, switch from the default Blocks coding interface to the Python Mode.

Copy the provided code into the code editor.

Step 3: Run the Script
Ensure your Quarky board is connected to the computer (usually via USB or Wi-Fi).

Click the Run button in the PictoBlox interface.

PictoBlox will typically open the Video Stage, showing the webcam feed and the ML model's real-time detections.

As you present your left hand or right hand (matching the poses you trained the model with) to the webcam, the corresponding gesture will be detected, and the Quarky robot will move left or right.

The code works by relying on the PictoBlox environment to handle the video stream, run the trained ML model, and feed the classification result into the Python script.
