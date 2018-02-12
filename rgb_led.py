#!/usr/bin/python
# coding=utf-8
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

red = 13
green = 15
blue = 16

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

try:
    c = int(raw_input('> RGB: '))
    GPIO.setup(red, c[0])
    GPIO.setup(green, c[1])
    GPIO.setup(blue, c[2])

except KeyboardInterrupt:
    print '\n\n[ Execution aborted ]'
except ValueError:
    print '\n[ Unexpected value ]'
except IndexError:
    print '\n[ Index out of range ]'
except TypeError:
    print '\n[ Only 0 or 1 number required ]'
finally:
    print '\nCleaning pins...'
    GPIO.cleanup()
