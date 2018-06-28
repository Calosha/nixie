import time
import json
import sys
from pprint import pprint
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#pin setup
#to do: move to settings.json
A = 6 
B = 19
C = 26
D = 13

PINGROUP = [D,C,B,A]
NUMBERS = ({'0': [0, 0, 0, 0],
			'1': [0, 0, 0, 1],
			'2': [0, 0, 1, 0],
			'3': [0, 0, 1, 1],
			'4': [0, 1, 0, 0],
			'5': [0, 1, 0, 1],
			'6': [0, 1, 1, 0],
			'7': [0, 1, 1, 1],
			'8': [1, 0, 0, 0],
			'9': [1, 0, 0, 1]})

def showDigit(digit, delay):
	GPIO.output(PINGROUP, NUMBERS[digit])
	time.sleep(delay)

def antiPoisoning():
	for i in range(10):
		GPIO.output(PINGROUP, NUMBERS[str(i)])
		time.sleep(0.2)
	for i in range(9, -1, -1):
		GPIO.output(PINGROUP, NUMBERS[str(i)])
		time.sleep(0.2)

GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)
while True:
	hr = time.strftime('%I')
	mn = time.strftime('%M')
	print('hour is ')
	print (hr)
	print('min is ')
	print(mn)
	if mn == '30' or mn == '00':
		antiPoisoning()

	for h in hr:
		showDigit(h,1)
	for m in mn:
		showDigit(m,1)
