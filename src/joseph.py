import RPi.GPIO as GPIO
import sys
import signal
from time import sleep

GPIO.setmode(GPIO.BCM)

LED = 2
SWITCH = 3

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def signal_handler(sig=None, frame=None):
    print('You pressed Ctrl+C!')
    GPIO.output(LED, 0)
    GPIO.cleanup()
    sys.exit(0)


# def toggle_light(code):
#     new_val = 1 - states[p]
#     GPIO.output(pins[p], new_val)
#     states[p] = new_val


signal.signal(signal.SIGINT, signal_handler)

last = -1

try:
    while True:
        new_val = GPIO.input(SWITCH)
        if new_val != last:
            print(f'New value: {new_val}')
            if new_val:
                GPIO.output(LED, 1)
            else:
                GPIO.output(LED, 0)

        last = new_val
        sleep(0.1)
        # line = sys.stdin.readline().rstrip()
        # print(line)
        # parts = line.split(' ')
        # print(parts)
        # for p in parts:
        #     if p not in ['r', 'y', 'g']:
        #         print(f'Ignoring: {p}')
        #     else:
        #         toggle_light(p)
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
