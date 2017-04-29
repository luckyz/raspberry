#!/usr/bin/python
# coding=utf-8
import RPi.GPIO as GPIO
from time import sleep
from os import system
from numpy.random import uniform

#from pudb import set_trace; set_trace()

# Pin physical numeration
GPIO.setmode(GPIO.BOARD)

# Configuration
# /////////////////////////////////////////////////////////

# Reactor's light channel
reactor = 7

# Winner player's light and button channels (light, button)
left_light = 15
left_button = 38
right_light = 16
right_button = 40

# Channels list
channels = (reactor, left_light, right_light)

# Countdown to start game
countdown = 3

# /////////////////////////////////////////////////////////

# Pinout
GPIO.setup(tuple(channels), GPIO.OUT)
GPIO.setup(left_button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(right_button, GPIO.IN, GPIO.PUD_UP)

# Variables
reactor_light = False
playing = False
on = False
time = 0


def poweron(pin):
	GPIO.output(pin, True)

def poweroff(pin):
	GPIO.output(pin, False)

def generate():
	return float('{0:.1f}'.format(uniform(0.3,2)))

def clear():
	return system('clear')

def left_button_pressed(channel):
	global on
	if on:
		p1.win()
	else:
		p2.win()

def right_button_pressed(channel):
	global on
	if on:
		p2.win()
	else:
		p1.win()

class Player:
	def __init__(self, light, button, name):
		self.light = light
		self.button = button
		self.points = 0
		self.name = name

	def win(self):
		self.points += 1

		clear()
		print '{} WIN!'.format(self.name)

		p = GPIO.PWM(self.light, 0.5)

		for i in range(0,3):
			p.start(0)
			for dc in range(0,101):
				p.ChangeDutyCycle(dc)
			for dc in reversed(range(0, 100, )):
				p.ChangeDutyCycle(dc)
		for i in range(0,3):
			GPIO.output(self.light, True)
			sleep(0.3)
			GPIO.output(self.light, False)
			sleep(0.3)

class Game:
	def __init__(self):
		self.light = reactor
		GPIO.output(reactor, False)

	def scoreboard(self):
		clear()

		global players
		number_of_players = sum([1 for player in players])
		print '========== SCOREBOARD =========='
		for player_number in range(number_of_players):
			player = players[player_number]
			print 'Player {0}: {1}'.format(player_number + 1, player.points)
		print '================================'
		raw_input('\n> [ Press key to continue ]\n')

	def start(self):
		global time
		time = generate()
		sleep(time)
		
		global on
		on = True
		poweron(reactor)
		time = generate()
		sleep(time)

		on = False
		poweroff(reactor)


if __name__ == '__main__':
	# Player creation
	p1 = Player(left_light, left_button, 'p1')
	p2 = Player(right_light, right_button, 'p2')

	# Participant players
	players = (p1, p2)

	try:
		while True:
			clear()
			# Wait before start
			for t in reversed(range(1, countdown + 1)):
				print 'Game starts in:\n{0}...'.format(t)
				sleep(1)
				clear()
			
			print '[ GAME STARTED! ]\n'
			playing = True
			
			while playing is True or (GPIO.input(left_button) == True) or (GPIO.input(right_button) == True):
				# Reactor light
				Game().start()

				if playing is True:
					if GPIO.input(left_button) == False:
						playing = False
						if on:
							p1.win()
							break
						else:
							p2.win()
							break
					elif GPIO.input(right_button) == False:
						playing = False
						if on:
							p2.win()
							break
						else:
							p1.win()
							break

			Game().scoreboard()

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
