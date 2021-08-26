# InverseKinematicsPi
This is an inverse kinematic model and code for my 4 dof robotic arm. It it controlled by a PCA9685 which in turn is controlled by a Raspberry Pi. The code is written purely in Python. Massive thanks to [Angela Sodemann](https://www.youtube.com/user/asodemann3) for her amazing videos behind the mathematics involved in inverse kinematics. Without them I probably never would've been able to get to this far. 

So at a high level, the way this works is pretty simple, it takes x, y, z and configuration input from the user and it later sends this input through a bunch of code that carries out a series of mathematical operations that return the angle at which the first 3 servos should rotate to. The angle at which the 4th servo would rotate to depends on the configuration set by the user. 

At the moment there are 3 fixed configurations: up, down and zero. Up makes the end effector look up at a complete 90 degrees, down makes the end effector look down at a negative 90 degrees and zero makes the end effector aligned with the servo at 0 degrees. 

Now for the more technical details of the robot. Each actuator has a frame of rotation and these frames are defined by a matrix depending on how they rotate. They are saved in variables in the code as R0_1, R1_2, etc. R0_1 would be the rotation matrix for the first servo, R1_2 for the second servo and so on all the way to R3_4 for the fourth servo. The fourth rotation matrix is the angular position of our end effector.

R0_4 is the rotation matrix of the 4th rotation matrix or end effector with respect to the base and this is what we will use mainly to find the configuration of the robot. R0_4 is defined as the product of all the other rotation matrices, i.e. R0_1 * R1_2 * R2_3 * R3_4. 

Now if we can somehow find the rotation matrices for the first 3 servos and R0_4, then we can find the rotation matrix of R3_4 by simple algebra, right? Right. So how do we find the first 3 rotation matrices and how do we find R0_4. Well we define R0_4 from the beginning as up, down and zero. These specific configurations have a specific roation matrix defined in the code, if we want more variations, maybe a 45 degree angle up or down then we need to define more rotation matrices from the beginning that depend on the 45 degree angle. 

We know what R0_4 is and now we need to find the first 3 rotation matrices. 
