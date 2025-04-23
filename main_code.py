import mbot2, event, time, cyberpi, mbuild

# Initialize variables
base_power = 40
kp = 0.7

def ultra():
    return mbuild.ultrasonic2.get(index=1)
    
    
@event.is_press('a')
def is_btn_press():
    cyberpi.stop_other()
    while True:
        l2_color = mbuild.quad_rgb_sensor.get_color_sta("L2")
        l1_color = mbuild.quad_rgb_sensor.get_color_sta("L1")
        r1_color = mbuild.quad_rgb_sensor.get_color_sta("R1")
        r2_color = mbuild.quad_rgb_sensor.get_color_sta("R2")
        if l2_color == "black" and l1_color == "black" and r2_color == "black" and r1_color == "black":
            mbot2.drive_power(0, 0)  # First stop the robot
            time.sleep(0.5)
            mbot2.drive_power(30, -30)
            time.sleep(0.75)
            mbot2.drive_power(0, 0)
            break
        else:
            # Fall back to black line following
            offset = mbuild.quad_rgb_sensor.get_offset_track(1)
            left_power = -1 * (base_power + kp * offset)
            right_power = base_power - kp * offset
            mbot2.drive_power(right_power, left_power)
    
def handle_white_line():
    white_line = cyberpi.quad_rgb_sensor.get_white_sta("all", 1)  
    if white_line == 6 or white_line == 4 or white_line == 2:
        mbot2.drive_power(30, -30)  # Move forward
        return True
    elif white_line == 8 or white_line ==12:
        mbot2.drive_power(9.5, -50)   # Turn left
        return True
    elif white_line == 3 or white_line == 1:
        mbot2.drive_power(50, -9.5)   # Turn right
        return True
    elif white_line ==7 or white_line==0:
        mbot2.drive_power(-15, 15)   # Turn right
        return True
    return False  # Only return False if no white line detected


@event.is_press('b')
def start_line_following():
    cyberpi.stop_other()
    while True:
        distance = ultra()
        
        if distance <= 15:
            mbot2.drive_power(0, 0)
        else:
            l2_color = mbuild.quad_rgb_sensor.get_color_sta("L2")
            l1_color = mbuild.quad_rgb_sensor.get_color_sta("L1")
            r1_color = mbuild.quad_rgb_sensor.get_color_sta("R1")
            r2_color = mbuild.quad_rgb_sensor.get_color_sta("R2")
        # First try white line detection
            if handle_white_line():
                pass
            else:
            # Fall back to black line following
                offset = mbuild.quad_rgb_sensor.get_offset_track(1)
                left_power = -1 * (base_power + kp * offset)
                right_power = base_power - kp * offset
                mbot2.drive_power(right_power, left_power)
        time.sleep(0.01)
        
