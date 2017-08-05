#!/usr/bin/python
# coding=utf-8
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

# data
channel = 7
freq = 50

GPIO.setup(channel, GPIO.OUT)

p = GPIO.PWM(channel, freq)  # channel=7 frequency=50Hz
p.start(0)
try:
    while True:
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
    p.stop()
    GPIO.cleanup()
