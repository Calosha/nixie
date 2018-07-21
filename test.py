import time
import json
import sys
from pprint import pprint
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#pin setup
#to do: move to settings.json

# Hours most significant
A = 6
B = 19
C = 26
D = 13

# Hours least significant
A1 = 12
B1 = 16
C1 = 20
D1 = 21

# Minutes most significant
A2 = 18
B2 = 23
C2 = 24
D2 = 25

# Minutes least significant
A3 = 4
B3 = 17
C3 = 27
D3 = 22

HRM = [D, C, B, A]
HRL = [D1, C1, B1, A1]
MNM = [D2, C2, B2, A2]
MNL = [D3, C3, B3, A3]

NUMBERS = ({'1': [0, 0, 0, 0],
			'0': [0, 0, 0, 1],
			'9': [0, 0, 1, 0],
			'8': [0, 0, 1, 1],
			'7': [0, 1, 0, 0],
			'6': [0, 1, 0, 1],
			'5': [0, 1, 1, 0],
			'4': [0, 1, 1, 1],
			'3': [1, 0, 0, 0],
			'2': [1, 0, 0, 1]})

def showDigit(digit, pingroup):
	GPIO.output(pingroup, NUMBERS[digit])
	time.sleep(delay)

def showTime(hours, minutes):
	print(hours)
	print(minutes)
	showDigit(hours[0], HRM)
	showDigit(hours[1], HRL)
	showDigit(minutes[0], MNM)
	showDigit(minutes[1], MNL)

def antiPoisoning():
	for i in range(10):
		GPIO.output(PINGROUP, NUMBERS[str(i)])
		time.sleep(0.2)
	for i in range(9, -1, -1):
		GPIO.output(PINGROUP, NUMBERS[str(i)])
		time.sleep(0.2)
#hours most
GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)

#hours least
GPIO.setup(A1, GPIO.OUT)
GPIO.setup(B1, GPIO.OUT)
GPIO.setup(C1, GPIO.OUT)
GPIO.setup(D1, GPIO.OUT)

#mins most
GPIO.setup(A2, GPIO.OUT)
GPIO.setup(B2, GPIO.OUT)
GPIO.setup(C2, GPIO.OUT)
GPIO.setup(D2, GPIO.OUT)

#mins least
GPIO.setup(A3, GPIO.OUT)
GPIO.setup(B3, GPIO.OUT)
GPIO.setup(C3, GPIO.OUT)
GPIO.setup(D3, GPIO.OUT)

while True:
	hr = time.strftime('%I')
	mn = time.strftime('%M')
	print('hour is ')
	print (hr)
	print('min is ')
	print(mn)
	if mn == '30' or mn == '00':
		antiPoisoning()
	time.sleep(1)
	showTime(hr,mn)
