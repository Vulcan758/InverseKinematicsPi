import pigpio
pi = pigpio.pi()

testpin = int(input("Which pin is for servo "))

try:
	while True:
		pulsewidth = int(input("Set pulsewidth "))
		pi.set_servo_pulsewidth(testpin, pulsewidth)

finally:
	pi.set_servo_pulsewidth(testpin, 0)
	pi.stop()
