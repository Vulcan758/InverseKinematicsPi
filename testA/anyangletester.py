from adafruit_servokit import ServoKit

n = 16

kit = ServoKit(channels = n)

while True:
    channel = int(input("Select channel "))
    angle = float(input("Select angle "))
    kit.servo[channel].angle = angle
    
