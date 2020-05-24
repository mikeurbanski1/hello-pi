import RPi.GPIO as GPIO
import sys
import signal
from time import sleep

GPIO.setmode(GPIO.BCM)

red = int(sys.argv[1])
yellow = int(sys.argv[2])
green = int(sys.argv[3])
pins = [red, yellow, green]


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    for pin in pins:
        GPIO.output(pin, 0)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
    GPIO.cleanup()

while True:
    try:
        GPIO.output(red, 1)
        sleep(2)
        GPIO.output(red, 0)
        GPIO.output(yellow, 1)
        sleep(1)
        GPIO.output(yellow, 0)
        GPIO.output(green, 1)
        sleep(2)
        GPIO.output(green, 0)
    except KeyboardInterrupt:
        print("Keyboard interrupt")
    except Exception as e:
        print(f"Some other error: {e}")
    finally:
        signal_handler()
