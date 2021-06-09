from adafruit_servokit import ServoKit
from time import sleep

n = 16

kit = ServoKit(channels = n)

def initialization():
    kit.servo[0].angle = 90
    kit.servo[1].angle = 155
    kit.servo[2].angle = 170
    kit.servo[3].angle = 10

        
def rotation(joint_num, desired_angle):
    current_angle = kit.servo[joint_num].angle
    print(current_angle)
    while current_angle != desired_angle:
        if current_angle > desired_angle:
            post_angle = current_angle - 5.0
            intpost_angle = int(post_angle)
            kit.servo[joint_num].angle = intpost_angle
            print(kit.servo[joint_num].angle)
            sleep(0.01)
        elif current_angle < desired_angle:
            post_angle = current_angle + 5.0
            intpost_angle = int(post_angle)
            kit.servo[joint_num].angle = intpost_angle
            print(kit.servo[joint_num].angle)
            sleep(0.01)
    new_angle = kit.servo[joint_num].angle
    print("The new angle is " + str(new_angle))

while True:
    joint_numb = int(input("Enter joint index would you like to control: "))
    angleb = int(input("Enter angle you would like it to rotate: "))
    initialization()
    kit.servo[joint_numb].angle = angleb
