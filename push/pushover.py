#!/usr/bin/python
# coding=utf-8
import httplib, urllib


# Add your data here
USER_KEY = ''
API_KEY = ''
MESSAGE = ''

conn = httplib.HTTPSConnection("api-newssl.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.urlencode({
    "token": "APP_KEY",
    "user": "USER_KEY",
    "message": "MESSAGE",
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()
