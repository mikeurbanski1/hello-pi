from flask import Flask
from flask_ask import Ask, statement
import RPi.GPIO as GPIO
from time import sleep
import random
import _thread

app = Flask(__name__)
ask = Ask(app, '/')


states = {'red': 0, 'yellow': 0, 'green': 0}


@ask.intent('LedIntent')
def led(color, status):
    print(f'Got request to turn {color} {status}')
    color = color.lower()
    status = status.lower()
    if color not in pins.keys():
        return statement("I don't have {} light".format(color))
    if status not in ['on', 'off']:
        return statement(f"I can't turn a light {status}")
    GPIO.output(pins[color], GPIO.HIGH if status == 'on' else GPIO.LOW)
    states[color] = 1 if status == 'on' else 0
    return statement('Turning the {} light {}'.format(color, status))


@ask.intent('RaveIntent')
def rave():
    print(f'Got request for a rave')
    _thread.start_new_thread(do_rave, ("Rave thread", ))
    _thread.
    return statement('Rave hard, my friend')


@ask.intent('StopRaveIntent')
def stop_rave():
    print(f'Got request for a rave')
    _thread.start_new_thread(do_rave, ("Rave thread", ))
    return statement('Rave hard, my friend')


def do_rave(thread_name):
    count = 0
    options = list(states.keys())
    while count < 50:
        color = random.choice(options)
        GPIO.output(pins[color], GPIO.HIGH if states[color] == 0 else GPIO.LOW)
        states[color] = 1 - states[color]
        count += 1
        sleep(0.2)


if __name__ == '__main__':
    try:
        print('setting up')
        GPIO.setmode(GPIO.BCM)
        pins = {'red': 2, 'yellow': 3, 'green': 4}
        for pin in pins.values():
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)
        app.run(debug=True)
    finally:
        print('Cleaning up')
        GPIO.cleanup()
