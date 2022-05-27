Final-Assignment
================================

Final assignment of the Research Track 1 course, development of a software architecture for the control of a mobile robot.
It's a Python code to control the movement of a robot inside a the given map which resembles a box with rooms. The user must choose a modality of control of the robot:
* autonomously reach a x,y coordinate inserted by the user.
* let the user drive the robot with the keyboard.
* let the user drive the robot assisting them to avoid collisions.

Installing and running
----------------------
Download (or even better, fork) the repository from: [CarmineD8/final_assignment](https://github.com/CarmineD8/final_assignment.git) and the [slam_gmapping](https://github.com/CarmineD8/slam_gmapping.git) package, having care to switch on the `noetic` branch.
The ros navigation stack
```bash
Apt-get install ros-<your_ros_distro>-navigation
```
is needed

After you download and build the workspace, make sure to make all the .py files in the scripts folder as executables:
```bash
chmod +x <name_pythonSript.py>
```

then run in three different shells the three launcher needed:
```bash
$ roslaunch final_assignment simulation_gmapping.launch
$ roslaunch final_assignment move_base.launch
$ roslaunch assignment_three launcher.launch
```

the first two launch files are launching a robotic simulation on Gazebo and Rviz, the last launch file is the one that executes the user interface with the explenation of the actions in the code.

Structure
-----------------------------
The logic of the code and how those three nodes communicate is written in the [flowchart](Final_flowchar.jpg).
The software rely on the move_baseand gmapping packages for localizing the robot and plan the motion.

In the input_controller.py code we find the functions to manage each user choice

### Mode 1 -choice1()- ###
Function to handle the autonomous reach of a point: takes the coordinates form the user and checks if the aimed target is reached, calls the service Directions and sends the coordinates to the manage_input(request) function in `choice1.py`.
The action of the move_base package is used, given a goal in the world, will attempt to reach it with a mobile base.

`manage_input(request)` : function to manage the user choice of mode 1. Sets the target and waits for the result.
`directions_server()` : initializes the node and calls the service handler

### Mode 2 and 3 -choice2() and choice3()- ###
Function to handle driving experience: calls the service to manage the input from keyboard, if the user selects mode 2 it will send 1 to the manage_input(request) function in choice2.py; if the user selects mode 3 it will send 2 to the manage_input(request) function in choice2.py

The teleop_twist_keyboard topic is used.

`manage_input(request)` : function called by both choice 2 and 3 but if mode 3 is choosen here the launcher for that specific mode is called.
    
   * `request.input_case == 1` : call keyboard teleop and the choice2.launch is launched.
    
   * `request.input_case == 2` : call keyboard teleop and the osbstacle avoidance and choice3.launch is launched.

`input_key_server()` : initializes the node and calls the service handler

Documentation
--------------
The Sphinx documentation for the whole code is available at the following link [Final_assignment_documentation](https://alicecatalano.github.io/Reasearcch-Track-1-Final-Assignment/)
