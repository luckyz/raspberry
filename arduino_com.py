#!/usr/bin/python
# coding=utf-8
import RPi.GPIO as GPIO
from time import sleep
import serial
import os
import urllib2
import json
from bs4 import BeautifulSoup
import requests
import re
import unicodedata
import threading


GPIO.setmode(GPIO.BOARD) # Physical pin numeration
button = 11	# Action button
GPIO.setup(button, GPIO.OUT) 

# Pushetta configuration
API_KEY = '90eb18ed01e35ee31418f4abf8031f8a113ddb45'
CHANNEL_NAME = 'rafaela_weather'
MESSAGE = ''

condition, temperature, real_feel, humidity, min_temp, max_temp = "", "", "", "", "", ""

def send_notification(token, channel, message):
	data = {
		"body" : message,
		"message_type" : "text/plain",
	}

	req = urllib2.Request('http://api.pushetta.com/api/pushes/{0}/'.format(channel))
	req.add_header('Content-Type', 'application/json')
	req.add_header('Authorization', 'Token {0}'.format(token))

	response = urllib2.urlopen(req, json.dumps(data))

def normalize_text(text):
	return ''.join((c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn'))

def get_weather():
	req = requests.get("http://www.accuweather.com/en/ar/rafaela/5992/current-weather/5992")
	status = req.status_code

	if status == 200:
		html = BeautifulSoup(req.text, "html.parser")

		data = html.find("div", {"class" : "info"})
		stats = html.find("ul", {"class" : "stats"})
		stats = stats.find_all("li")
		table = html.find("div", {"id" : "feature-history"})
		table = table.find_all("td")

		pattern = re.compile("\d+")

		global condition, temperature, real_feel, humidity, min_temp, max_temp

		condition = html.find("span", {"class":"cond"}).getText()
		temperature = html.find("strong", {"class":"temp"}).getText()
		temperature = pattern.search(normalize_text(temperature))
		temperature = temperature.group(0)
		real_feel = html.find("span", {"class":"realfeel"}).getText()
		real_feel = pattern.search(normalize_text(real_feel))
		real_feel = real_feel.group(0)
		humidity = pattern.search(stats[0].getText())
		humidity = humidity.group(0)
		max_temp = pattern.search(table[0].getText())
		max_temp = max_temp.group(0)
		min_temp = pattern.search(table[4].getText())
		min_temp = min_temp.group(0)

def send_to_arduino(data):
	arduino = serial.Serial('/dev/ttyACM0', 9600)
	for item in data:
		arduino.write(item)	# Send each item from data object to Arduino
	arduino.close() # End communication

try:
	os.system("clear")
	print "Rafaela Weather Forecast\n\n> Waiting for a button pressing..."
	
	t = threading.Thread(target=get_weather)
	t.start()

	while True:
		if GPIO.output(button, False):
			os.system("clear")
			print "Rafaela Weather Forecast\n\n"
			print "[+] Getting external data from http://www.accuweather.com/"
			# cond, temp, rf, humidity, mint, maxt = get_weather()
			MESSAGE = "Current temperature: {0}°C. | Min: {1}°C - Max: {2}°C\
.\nReal feel: {3}°C. | Humidity: {4}%.\
".format(temperature, min_temp, max_temp, real_feel, humidity)
			# MESSAGE = "Current temperature: {0}°C.\nHumidity: {1}%.".format(temp, humidity)
			print "[+] Sending data to Arduino..."
			# send_to_arduino((temp, humidity, mint, maxt, rf, cond))
			send_to_arduino((temperature, humidity))
			print "[+] Sending Pushetta notification..."
			send_notification(API_KEY, CHANNEL_NAME, MESSAGE)
			print "> Data sent!\n{0}\n{1}\n{0}\n".format("=" * 80, MESSAGE)
			print "> Waiting for a button pressing..."

except KeyboardInterrupt:
	print '\nCleaning pins...'
	print '\n\n[ Execution aborted ]'
except ValueError:
	print '\nCleaning pins...'
	print '\n[ Unexpected value ]'
except IndexError:
	print '\nCleaning pins...'
	print '\n[ Index out of range ]'
except TypeError:
	print '\nCleaning pins...'
	print '\n[ Types do not match ]'
finally:
	GPIO.cleanup()
