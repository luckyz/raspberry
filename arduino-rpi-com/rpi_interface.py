#!/usr/bin/python
# coding=utf-8
import RPi.GPIO as GPIO
import serial
#from time import sleep


GPIO.setmode(GPIO.BOARD) # Physical numeration pins
# pin = 7
# GPIO.setup(pin, GPIO.OUT)

try:
	# ser = ser = serial.Serial('/dev/cu.usbmodem1411', 9600) # for Mac OS X
	ser = serial.Serial('/dev/ttyACM0', 9600) # for Raspberry Pi
	ser.write('foo')
    while True:
        None # Write code here
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
