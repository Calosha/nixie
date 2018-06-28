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
NUMBERS = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001'}

def showDigit(digit, delay):
	binary = NUMBERS[digit]
	for i in range(4):
		pin = PINGROUP[i]
		intval = int(binary[i]) #converting string to int
		GPIO.output(pin, intval)
		time.sleep(delay)

GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)
while True:
	hr = time.strftime('%I')
	mn = time.strftime('%M')
	for h in hr:
		showDigit(h,1)
	for m in mn:
		showDigit(m,1)