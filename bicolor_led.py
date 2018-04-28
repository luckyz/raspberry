#!/usr/bin/python
# coding=utf-8
import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD) # pin physical numeration
red = 11
green = 13
GPIO.setup((red, green), GPIO.OUT)

try:
    valor = False
    while True:
    	GPIO.output(red, valor)
        GPIO.output(red, not valor)
        valor = not valor
	sleep(1)

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
