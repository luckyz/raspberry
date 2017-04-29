#!/usr/bin/python
# coding=utf-8
import urllib2
import json


# Add your data here
API_KEY = ''
CHANNEL_NAME = ''
MESSAGE = ''

def sendNotification(token, channel, message):
	data = {
		"body" : message,
		"message_type" : "text/plain",
	}

	req = urllib2.Request('http://api.pushetta.com/api/pushes/{0}/'.format(channel))
	req.add_header('Content-Type', 'application/json')
	req.add_header('Authorization', 'Token {0}'.format(token))

	response = urllib2.urlopen(req, json.dumps(data))

sendNotification(API_KEY, CHANNEL_NAME, MESSAGE)
