from adafruit_servokit import ServoKit

n = 16

kit = ServoKit(channels = n)

base = 0
shoulder = 1
elbow = 2
wrist = 3

limbs = [base, shoulder, elbow, wrist]

def rotate(the_limb, angle):
	kit.servo[the_limb].angle = angle

def rotation():

