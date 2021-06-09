from adafruit_servokit import ServoKit
from time import sleep
import numpy as np

n = 16

kit = ServoKit(channels = n)


a_1 = 5.25
a_2 = 11.80
a_3 = 7.0
a_4 = 5.25

def inverseKinematicModel(x, y, z, a_1, a_2, a_3, a_4):
    
    theta_0 = np.arctan2(y, x)
    r_1 = np.sqrt( x**2 + y**2 )

    r_2 = np.sqrt( (z - a_1)**2 - r_1**2)
    phi = np.arctan2( (z - a_1), r_1 )
    p = a_4**2 - (r_2 - a_3)**2 - a_2**2
    o = -2 * (r_2 - a_3) * a_2
    phi_2 = np.arccos( p / o )

    theta_1 = phi - phi_2

    c_1 = 180 - 90 - phi_2

    k = a_2**2 - (r_2 - a_3)**2 - a_4**2
    l = -2 * (r_2 - a_3) * a_4

    c_3 = np.arccos( k / l )
    c_2 = 180 - 90 - c_3

    theta_3 = 180 - c_1 - c_2

    phi_3 = 90 + c_1
    theta_2 = 180 - phi_3

    return theta_0, theta_1, theta_2, theta_3

def initialization():
    kit.servo[0].angle = 90
    kit.servo[1].angle = 135
    kit.servo[2].angle = 170
    kit.servo[3].angle = 10

def smoother(end, delta, joint):
    start = kit.servo[joint].angle 
    incmove = (end - start)/100.0
    inctime = delta/100.0
    for x in range(100):
        kit.servo[joint].angle = start + x * incmove
        sleep(inctime)


initialization()
delta = 1

while True:
    x = int(input("Enter the x-coordinates: "))
    y = int(input("Enter the y-coordinates: "))
    z = int(input("Enter the z-coordinates: "))

    theta_0, theta_1, theta_2, theta_3 = inverseKinematicModel(x, y, z, a_1, a_2, a_3, a_4)
    smoother(theta_0, delta, 0)
    smoother(theta_1, delta, 1)
    smoother(theta_2, delta, 2)
    smoother(theta_3, delta, 3)

    
    
