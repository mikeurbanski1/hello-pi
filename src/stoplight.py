import RPi.GPIO as GPIO
import sys
import signal
from time import sleep

GPIO.setmode(GPIO.BCM)

red = int(sys.argv[1])
yellow = int(sys.argv[2])
green = int(sys.argv[3])
pins = {'r': red, 'y': yellow, 'g': green}


def signal_handler(sig=None, frame=None):
    print('You pressed Ctrl+C!')
    for pin in pins.values():
        GPIO.output(pin, 0)
    GPIO.cleanup()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

for pin in pins.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

states = {'r': 0, 'y': 0, 'g': 0}


try:
    while True:
        line = sys.stdin.readline()
        parts = line.split(' ')
        for p in parts:
            if p not in ['r', 'y', 'g']:
                print(f'Ignoring: {p}')
            else:
                new_val = 1 - states[p]
                GPIO.output(pins[p], new_val)
                states[p] = new_val
        # GPIO.output(red, 1)
        # sleep(2)
        # GPIO.output(red, 0)
        # GPIO.output(yellow, 1)
        # sleep(1)
        # GPIO.output(yellow, 0)
        # GPIO.output(green, 1)
        # sleep(2)
        # GPIO.output(green, 0)

except Exception as e:
    print(f"Error: {e}")
    signal_handler()
