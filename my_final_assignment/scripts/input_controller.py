#! /usr/bin/env python
"""
.. module:: input_controller
   :platform: Unix
   :synopsis: Python code to create the user interface 
.. moduleauthor:: Alice Maria Catalano <s5157341@studenti.unige.it>

Service:
   /directions
   /input_key

This node implements the user interface, takes the user input and launches the specific launch file.
"""


import rospy
from assignment_three.srv import Directions		
from assignment_three.srv import Input_keyboard


def userInterface():
    """
    Function to print the text to show to the user.
    
    Returns:
    *input(String)* value from the user to send it to the menage service.
    """
    
    print("Hello User! please select between the different modalities:")
    print("1) automatic reach of the coordinates chosen by you")
    print("2) driving a robot experience")
    print("3) learn to drive, collision handler active")
    print("0) quit")
    print()        
    return input("input your choice: ")

def choice1():
    """
    Function to handle the first modality of moving the robot, asking to the user the coordinates.
    
    Service:
        /directions
    
    The user message is passed to the service ``manage_input``, advertised by :mod:`choice1` 
    """
    
    print("mode 1")
    x = float(input("insert x: "))
    y = float(input("insert y: "))
    
    rospy.wait_for_service('directions')
    directions = rospy.ServiceProxy('directions', Directions)
    aim= directions(x , y)
    
    if aim.return_== 1:
    	print("target reached successfully!")
    else:
    	print("target not reached")

         	
def choice2():
    """
    Function to handle the second modality of moving the robot, asking the user to directly drive the robot sending value 1.
    
    Service:
        /input_key
    
    The user choice is passed to the service ``manage_input``, advertised by :mod:`choice2` 
    """
    
    print("mode 2")
    rospy.wait_for_service('input_key')
    usrInput = rospy.ServiceProxy('input_key', Input_keyboard)
    usrInput(1)

def choice3():
    """
    Function to handle the third modality of moving the robot, asking the user to directly drive the robot sending value 2.
    
    Service:
        /input_key
    
    The user choice is passed to the service ``manage_input``, advertised by :mod:`choice2` 
    """
    
    print("choice 3")
    rospy.wait_for_service('input_key')
    usrInput = rospy.ServiceProxy('input_key', Input_keyboard)
    usrInput(2)


 
if __name__=="__main__":
    """
    This function initializes the ROS node, prints the interface and waits for the user to input his choice saving it in the 
    variable: mode(int)
    """ 
    rospy.init_node('main_controller')
    flag = 1
    
    while(flag):
        mode = userInterface()
        
        if mode.isnumeric():
            mode = int(mode)
            if (mode == 1):
                choice1()
            
            elif (mode == 2):
                choice2()  
            
            elif (mode == 3):
                choice3()
            
            elif (mode == 0):
                flag = 0
                print("press ctrl-C to quit")
                print()
            
            else:
                print("incorrect input!!")
        else:
            print("input value is not a number!!")
