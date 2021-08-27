# InverseKinematicsPi
This is an inverse kinematic model and code for my 4 dof robotic arm. It it controlled by a PCA9685 which in turn is controlled by a Raspberry Pi. The code is written purely in Python. Massive thanks to [Angela Sodemann](https://www.youtube.com/user/asodemann3) for her amazing videos behind the mathematics involved in inverse kinematics. Without them I probably never would've been able to get to this far. 

So at a high level, the way this works is pretty simple, it takes x, y, z and configuration input from the user and it later sends this input through a bunch of code that carries out a series of mathematical operations that returns the angle at which each servo should rotate to. The angle at which the 4th servo would rotate to depends on the configuration set by the user. 

At the moment there are 3 fixed configurations: up, down and zero. Up makes the end effector look up at a complete 90 degrees, down makes the end effector look down at a negative 90 degrees and zero makes the end effector aligned with the servo at 0 degrees. 

Now for the more technical details of the robot. Every robotic arm has a position and an orientation factor. From my understanding, the first 3 actuators in a robotic arm are usually concerned with the positioning of the end effector while the actuators after that are concerned with what the orientation of the end effector is. 

You can think of the orientation of the end effector as which way the ending link of the arm would look (e.g. left, right, up, down, straight, a little up, a little down, etc) and the positioning of the end effector can be thought of as where exactly the link would be placed. 

Each actuator has a frame of rotation and these frames are defined by a matrix depending on how they rotate. They are saved in variables in the code as R0_1, R1_2, etc. R0_1 would be the rotation matrix for the first servo, R1_2 for the second servo and so on all the way to R3_4 for the fourth servo. The fourth rotation matrix is the angular position of our end effector.

R0_4 is the rotation matrix of the 4th rotation matrix or end effector with respect to the base and this is what we will use mainly to find the configuration of the robot. R0_4 is defined as the product of all the other rotation matrices, i.e. R0_1 * R1_2 * R2_3 * R3_4. 

Now if we can somehow find the rotation matrices for the first 3 servos and R0_4, then we can find the rotation matrix of R3_4 by simple algebra, right? Right. So how do we find the first 3 rotation matrices and how do we find R0_4. Well we define R0_4 from the beginning as up, down and zero. These specific configurations have a specific roation matrix defined in the code, if we want more variations, maybe a 45 degree angle up or down then we need to define more rotation matrices from the beginning that depend on the 45 degree angle. 

We know what R0_4 is and now we need to find the first 3 rotation matrices. If you look at the matrices defined in the code, they all have a variable theta, this variable is angle at which the servo on each link should rotate to. Once we find those angles, we plug those into the rotation matrix and do what we have to do later on. 

How do we find each theta? We do this by taking a geometric approach to the whole arm up to the third servo. We do not use the 4th servo as that is only concerned with the orientation of the end effector. Using some simple trigonometry as shown in the code, we are able to find theta 1, 2 and 3.

Now that we've found it, we can find out what R3_4 has to be and from there we can find theta 4 for the fourth servo. 

After all these angles are found, the angle values are sent to the servos via Adafruit_ServoKit through the PCA9685 and then to the servos. Allowing your arm to be at the position you please. Now manually entering coordinates at which your arm should go to is not ideal and efficient. We can't exactly tell where exactly in space we want to go, we cant do that efficiently at least. To combat this, we use cameras where we can use image mapping to translate pixel values to real world coordinates. This is something I have done in another repository you can check out [here](https://github.com/Vulcan758/Rover)!
