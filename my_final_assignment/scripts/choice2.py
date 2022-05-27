#! /usr/bin/env python
"""
.. module:: choice2
   :platform: Unix
   :synopsis: Python code to let the user drive the robot
.. moduleauthor:: Alice Maria Catalano <s5157341@studenti.unige.it>

Service:
    /input_key

This node implements the lauching of the last 2 modalities:
   mode2. the user is free to drive the robot as he/her prefers without any constraint
   mode3. the user drives the robot but there will be a collision control, avoiding the user to hit obstacles.
"""
import rospy
from assignment_three.srv import Input_keyboard	
import os   

def manage_input(request):
    """
    Function called by both choice 2 and 3 but if mode 3 is choosen here the launcher for that specific mode is called.
    
    Args:
        *request(float64 x, float64 y)* coming from the move_base_msgs
    
    The user choice is passed to the `os` to launch the chosen launch file.
    """
    
    if request.input_case == 1:
       os.system("roslaunch assignment_three choice2.launch") 
       
    elif request.input_case == 2:
        print("calling teleop twist keyboard with obstacle avoidance control")
        os.system("roslaunch assignment_three choice3.launch")
    else:
        print("wrong parameter")
    return 0         
   
def input_key_server():
    """
    Function that describes the node `keyboard_controller` to the user.
    
    calls the service handler to manage the `input_key` service, retriving the values from the `manage_input` function.
    """
    
    print("driving experience node, DO NOT CLOSE THE TERMINAL")
    rospy.init_node('keyboard_controller')
    
    service = rospy.Service('input_key', Input_keyboard, manage_input)
    print("service ready")
    rospy.spin()


if __name__=="__main__":
    input_key_server()
