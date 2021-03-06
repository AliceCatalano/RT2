First-Assignment Research Track2
================================

The first assignment is devided in three parts:.
* Creating a full documentation using Sphinx or Doxygen for the [RT1 final assignment code](https://github.com/AliceCatalano/Research-Track-1-Final-Assignment.git).
* Create a jupiter notebook to initialize a new interface to drive the robot following the [final assignment requests](https://github.com/AliceCatalano/Research-Track-1-Final-Assignment.git).
* Perform a statistical analysis comparing [my solution](https://github.com/AliceCatalano/Research-Track-1-Assignment-1.git) for the first assignment of RT1 and the [given solution](https://github.com/CarmineD8/python_simulator.git).

First Task
----------------------
In this part of the work, after installing Sphinx and ReadTheDocs theme, I just commented the codes of the previous assignment, and the page with all the documentation was created.  
All the new documentation can be found in [this link](https://alicecatalano.github.io/RT2/).

Second Task
-----------------------------
In this task a user interface through Jupyter netbook was implemented. With this interface the user will be able to:
* Move the robot automatically to any coordinates
* Move the robot with a screen buttons interface
* Move the robot with the same buttons interface but with collision avoidance.

**Installing and executing**  
First of all check that all the python scripts are executable, otherwise execute
```
chmod +x <file.py>
```
Then from the Linux shell open three different tabs to execute
```shell
roslaunch final_assignment simulation_gmapping.launch
roslaunch final_assignment move_base.launch
roslaunch my_final_assignment jr_launcher.launch
```
Finally, in the Jupyter notebook page run all the cells of the `rt2_assignment1_b.ipynb`

### Mode 1  ###
For this interface the user just insert any kind of coordinate, and presses on the `start` button and will see the robot move.  
At the same time the position of the robot will be printed in real time in a 2D graph, just like the scanning of the laser present on the robot. At the end, every reached or not reached position will be plotted in a histogram to check on the efficiency of the code.  
In particular, for this function it was needed a change in the code used in the first assignment `choice1.py` because for further positions the robot wouldn't be able to arrive because of the restricted waiting time of the _Direction_ service.  
All the output graphs are displayed unther the choice menu.

### Mode 2 and 3 ###
In this modalities the robot is drove by the user with the buttons on the screen, which are intuitive and with a simple checkbox the user can initialize the collision avoidance function, that will stop the robot if a collision is suspected. This functionality is guarateed by a flag inserted in the new version of the code, now called `choice3_rt2.py`. Also the user can choose the speed of the robot through the slider widget.  
In these two cases the position and scanning of the robot is displayed in a 3D environment. 

Third Task
------------------
As last task a statistical analysis was required, comparing the codes of the first assignment which links are given at the beginning of this Readme file, while the Execel spreasheed is uploaded [in this repository](Statistical Analysis.xlsx). For each test 25 samples from both the algorithm were taken.
I decided to compare:  

**Speed of the two codes**  
This is a parametric test, in which the relevant test statistic, t, is calculated from the sample data and then compared with its probable value based on t-distribution at a specified level of significance for concerning degrees of freedom for accepting or rejecting the null hypothesis (H0: the codes work at the same speed).  
If the H0 can be rejected then I can support the alternative hypothesis (Ha: my code is faster).  
The time was registered in seconds and the calculations are made based on this data.  
Since in this case the t_calculated > t_from_table it can reject the H0 and support the Ha.

**Wrong Turns**  
For this I did the same parametric test, and for wrong turn I mean all the time the robot fixes its trajectory, starting a "zigzag" route.  
In this case  
H0: would be that both the code have the same efficiency in taking a straight route  
Ha: Professor's code is more efficient in taking a straight route.  
Through the t-test we get the same result as before so t_calculated > t_from_table it can reject the H0 and support the Ha.

**Crash test**  
This is a non-parametric test, and in this case the Chi-square test is used, in which we are going to compare the difference that exists between my observed counts and
the counts that would be expected if there were no relationship at all in the population.  
In this case the comparison is on the count of how many laps _myCode_ and the _profCpde_ had a system crash or an infinite loop event that forced the interruption of the execution of the code.  
H0: both code have the same efficiency  
Ha: Professor's code is more efficient.
From the result it's seeable that the probability of error obtained in rejecting the null hypothesis is really low, so I can rejected easily.

**Conclusions**  
From the data gathered in the different laps, it's evident that both code are efficient and the problems faced during the execution are more related to a system problem that to a poor algorithm. The difference between the two codes was never too large:
* In the time mesurements the difference is due to the different set uo of the robot velocity, so it's not related to the code structure
* In the path adjustment evaluation the difference is due to a better usage of the sensors' data, so the Professor robot is smarter on this level
* In the crash test both of the algorithm had some laps in which they were stuck but with different frequencies.

From this evaluation is easy to state that the Professor code is more efficient and reliable.
