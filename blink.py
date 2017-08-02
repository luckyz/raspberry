#!/usr/bin/python
# coding=utf-8
import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD) # Physical numeration pins
pin = 7
GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, 50)  # channel=7 frequency=50Hz
p.start(0)
try:
    while True:
            p.ChangeDutyCycle(100)
            sleep(0.1)
            p.ChangeDutyCycle(0)
            sleep(0.1)
except KeyboardInterrupt:
    print '\n\n[ Execution aborted ]'
except ValueError:
    print '\n[ Unexpected value ]'
except IndexError:
    print '\n[ Index out of range ]'
except TypeError:
    print '\n[ Required values: 0 or 1 ]'
finally:
    GPIO.cleanup()
