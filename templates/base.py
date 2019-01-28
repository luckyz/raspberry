#!/usr/bin/python
# coding=utf-8
import RPi.GPIO as GPIO
#from time import sleep


GPIO.setmode(GPIO.BOARD) # Physical numeration pins
# pin = 7
# GPIO.setup(pin, GPIO.OUT)

try:
    while True:
        None # Write code here
except Exception as e:
    print str(e)
finally:
    GPIO.cleanup()
