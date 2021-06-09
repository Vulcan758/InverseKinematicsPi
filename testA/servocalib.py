from adafruit_servokit import ServoKit
from time import sleep
kit = ServoKit(channels = 16)

n = 16

while True:
    #angle = int(input("what should the angle be? "))

    for number_of_servos in range(n):
     #   kit.servo[number_of_servos].angle = angle
        for i in range(180):
            kit.servo[number_of_servos].angle = i
            sleep(0.01)
