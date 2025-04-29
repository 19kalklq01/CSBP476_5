# Autonomous Line-Following Robot (mBot2)

![robot](https://github.com/user-attachments/assets/49104c6e-4afc-4ef6-af53-b64952635b35)

Project Overview
This project demonstrates an autonomous robot using the mBot2 to navigate a predefined track in the fastest time possible. The robot earns points by successfully reaching milestones while remaining fully autonomous, balancing speed optimization and accurate line tracking.

Contents of this Repository:
1. main_code.py: Source code for the mBot2 robot.
2. flowchart.png: Flowchart representing the logic of the code.
3. video.mp4: Local copy of the robot demonstration.
4. YouTube Video: Link to watch the robot completing the task.


FLOWCHART

![Flowchart (1)](https://github.com/user-attachments/assets/46373e6f-18d6-4ecc-ae13-65b7ba868f71)

Flowchart Description: 
1. Start: The program starts.
2. Measure Distance: The robot measures the distance from an object using an ultrasonic sensor.
3. Is Distance ≤ 15 ?: 
- if yes: The robot stops its motors.
- if No: The robot continues operating.
--Read L2,L1,R1,R2 color: The robot reads color sensor values (L2,L1,R1,R2) to identify the position of the line and modify its movement to remain on track.
--Is handle_white_line() = true?
---if yes: The robot  moves according to handle_white_line() function.
---if no: The robot gets the offset which shows how far it has deviated from the target line. Based on the offset the robot calculates the left and right power of the motors and then it will drive using the calculated left power and right power.

Wait 0.01 seconds: the robot waits for 0.01 seconds before looping back to measure distance. 






Team members:
- Hajar  Alnaqbi
- Alia Alkaabi
- Maryam Alderei
- Hessa Aldhaheri

