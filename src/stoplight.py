import RPi.GPIO as GPIO
import sys
from time import sleep

GPIO.setmode(GPIO.BCM)

red = int(sys.argv[1])
yellow = int(sys.argv[2])
green = int(sys.argv[3])

for pin in [red, yellow, green]:
    GPIO.setup(pin, GPIO.OUT)

while True:
    GPIO.output(red, 1)
    sleep(2)
    GPIO.output(red, 0)
    GPIO.output(yellow, 1)
    sleep(1)
    GPIO.output(yellow, 0)
    GPIO.output(green, 1)
    sleep(2)
    GPIO.output(green, 0)
