#! /usr/bin/env python
"""
.. module:: choice3
   :platform: Unix
   :synopsis: Python code to let the user drive the robot safely 
.. moduleauthor:: Alice Maria Catalano <s5157341@studenti.unige.it>

Subscribes to:
    /remap_cmd_vel to send the velocity in different cases based on the scanning
    /scan to get the laser scanning of the map

Publishes to:
    /cmd_vel the desired distance from the obstacles deteced.

This node implements the driving of the robot with obstacle avoidance.
"""
import rospy
import numpy
from geometry_msgs.msg import Twist, Vector3    #for cmd_vel topic
from sensor_msgs.msg import LaserScan           #for scan topic

threshold = 0.5

init = Vector3(0, 0, 0)
repost = Twist( init, init)

def minimum_th(ranges):
    """
    Function to section the ranges array in 3 parts and store the minimum distance for each of them.
    
    Args:
        *ranges* array of integers coming from the `LaserScan` topic
    
    Returns:
        *distance* array of integers containing the minimum distance from the right, center and left scanned ranges
    
    The user choice is passed to the `os` to launch the chosen launch file.
    """
    
    distance= [0,0,0]
    right = ranges[0:240]
    center = ranges[240:480]
    left = ranges[480:721]
    
    distance[0] = min(right)
    distance[1] = min(center)
    distance[2] = min(left)
    return distance
        
def clbk_scan(data):
    """
    Callback to compute the minimun obstacle distance to the right, left and in front of the robot.
    
    Args:
        *data* variable name for the message that is passed in, in this case the sensor_msgs
    
    Returns:
        *repost* global variable that modifies the velocity of the robot based on its position
    
    The publisher is initialized and publishes on the `repost` variable
    """
    global repost
    pub= rospy.Publisher('cmd_vel',Twist, queue_size=10)
    
    distances = minimum_th(data.ranges)
    flag_control = rospy.get_param("/obstacle_avoidance")
    if distances[0] < threshold :
        if repost.angular.z < 0 :
            repost.angular.z = 0    
    
    if distances[1] < threshold:
        if repost.linear.x > 0 :
            repost.linear.x = 0
    
    if distances[2] < threshold :
        if repost.angular.z > 0 :
            repost.angular.z = 0
    
    pub.publish(repost)

def clbk_remap(data):
    """
    Callback to copy the remap_cmd_vel on repost which can be modified or left untouched
    
    Args:
        *data* variable name for the message that is passed in, in this case the geometry_msgs
    """
    
    global repost
    repost = data
  
def inputKey_remap():
    """
    Function to initialize the node `inputKey_node`.
    Subscribes to the topics `Twist` and `LaserScan`.
    """
    rospy.init_node('inputKey_node')
    rospy.Subscriber("/remap_cmd_vel", Twist, clbk_remap)
    rospy.Subscriber("/scan", LaserScan, clbk_scan)
    rospy.spin()
    

if __name__=="__main__":
    inputKey_remap()
