from flask import Flask
from flask_ask import Ask, statement
import RPi.GPIO as GPIO
from time import sleep

app = Flask(__name__)
ask = Ask(app, '/')


@ask.intent('LedIntent')
def led(color, status):
    print(f'Got request to turn {color} {status}')
    if color.lower() not in pins.keys():
        return statement("I don't have {} light".format(color))
    GPIO.output(pins[color], GPIO.HIGH if status == 'on' else GPIO.LOW)
    return statement('Turning the {} light {}'.format(color, status))


if __name__ == '__main__':
    try:
        print('setting up')
        GPIO.setmode(GPIO.BCM)
        pins = {'red': 2, 'yellow': 3, 'green': 4}
        for pin in pins.values():
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)
        sleep(2)
        app.run(debug=True)
    finally:
        print('Cleaning up')
        GPIO.cleanup()
