from adafruit_servokit import ServoKit
from time import sleep
n = 16

kit = ServoKit(channels = n)

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

while True:
    joint_in = int(input("Select joint number "))
    endpoint = int(input("Select ending angle "))
    time_taken = 1 
    

    smoother(endpoint, time_taken, joint_in)
    
    
    
