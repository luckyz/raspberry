#!/usr/bin/python
# coding=utf-8
import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD) # physical numeration of pins
GPIO.setup(7, GPIO.OUT)

try:
    for dc in range(0, 101, 5):
        p.ChangeDutyCycle(dc)
        time.sleep(0.1)
    for dc in range(100, -1, -5):
        p.ChangeDutyCycle(dc)
        time.sleep(0.1)

except KeyboardInterrupt:
    print '\n\n[ Execution aborted ]'
except ValueError:
    print '\n[ Unexpected value ]'
except IndexError:
    print '\n[ Index out of range ]'
except TypeError:
    print '\n[ Only 0 or 1 number required ]'
finally:
    GPIO.stop()
    print '\nCleaning pins...'
    GPIO.cleanup()
