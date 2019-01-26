import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, False)

n=0

while True:
	n=n+1
	GPIO.output(11, True)
	sleep(1)
	GPIO.output(11, False)
	sleep(1)
	n=str(n)
	print("led has turned on " + n + " times")
	n=int(n)
	if n==5:
		break
print("press any to close program")

print("I tried adding this at my pc.")
end=input(), exit
