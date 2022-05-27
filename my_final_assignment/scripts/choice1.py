#! /usr/bin/env python
"""
.. module:: choice1
   :platform: Unix
   :synopsis: Python code to move the robot to the coordinates given by the user 
.. moduleauthor:: Alice Maria Catalano <s5157341@studenti.unige.it>

Service:
    /directions

Action:
    /move_base
    /actionlib

This node implements the automatic movement of the robot from it's current/initial position, to the one inserted by the user
evaluating if it is reachable or not.
"""
import rospy
from assignment_three.srv import Directions 

import actionlib
from move_base_msgs.msg import *
from actionlib_msgs.msg import *
 
def manage_input(request):
    """
    Function to handle the user choice of mode 1. Sets the target and waits for the result.
    
    Args:
        *request(float64 x, float64 y)* coming from the move_base_msgs
    
    Returns:
        1 : when the goal is reached
        -1: when the goal is not reached or not reachable
    
    The user choice is passed to the action parameters, send to the server with `target` variable and waits to check if the choosen point can be reached or not (in this case will call the cancel_goal() function)
    """
    #function to manage the user choice of mode 1. Sets the target and waits for the result
    
    x = request.x
    y = request.y
    print("going to point x: ",x," y: ",y)
    
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()
    target = MoveBaseGoal()
    
    target.target_pose.header.frame_id = 'map'
    target.target_pose.pose.orientation.w = 1
    target.target_pose.pose.position.x = x
    target.target_pose.pose.position.y = y
    
    client.send_goal(target)
    
    wait = client.wait_for_result(timeout=rospy.Duration(150.0))
    
    if not wait:
        
        print("the point can't be reached!")
        client.cancel_goal()
        return -1
    
    print("Arrived at destination")
    return 1

def directions_server():
    """
    Function that describes the node `directions_controller` to the user.
    
    calls the service handler to manage the `directions` service, retriving the values from the `manage_input` function.
    """
    
    print("automatic motion node, DO NOT CLOSE THE TERMINAL")
    rospy.init_node('directions_controller')
    
    s = rospy.Service('directions', Directions, manage_input)
    print("service ready")
    rospy.spin()

if __name__=="__main__":
    directions_server() 
