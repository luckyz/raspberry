#!/usr/bin/python
# coding=utf-8
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

red = 33
green = 35
blue = 37

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

try:
    c = raw_input('> RGB: ')

    while True:
        GPIO.output(red, int(c[0]))
        GPIO.output(green, int(c[1]))
        GPIO.output(blue, int(c[2]))

        c = raw_input('> RGB: ')

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
