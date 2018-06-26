import time
import json
from pprint import pprint
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#pin setup
#to do: move to settings.json
A = 6 
B = 19
C = 26
D = 13
GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)
while True:
	#0
	GPIO.output(D, 0)
	GPIO.output(C, 0)
	GPIO.output(B, 0)
	GPIO.output(A, 0)
	time.sleep(1)
	#1
	GPIO.output(D, 0)
	GPIO.output(C, 0)
	GPIO.output(B, 0)
	GPIO.output(A, 1)
	time.sleep(1)
	#2
	GPIO.output(D, 0)
	GPIO.output(C, 0)
	GPIO.output(B, 1)
	GPIO.output(A, 0)
	time.sleep(1)
	#3
	GPIO.output(D, 0)
    GPIO.output(C, 0)
    GPIO.output(B, 1)
    GPIO.output(A, 1)
	time.sleep(1)
	#4
    GPIO.output(D, 0)
    GPIO.output(C, 1)
    GPIO.output(B, 0)
    GPIO.output(A, 0)
	time.sleep(1)
	#5
    GPIO.output(D, 0)
    GPIO.output(C, 1)
    GPIO.output(B, 0)
    GPIO.output(A, 1)
	time.sleep(1)
	#6
    GPIO.output(D, 0)
    GPIO.output(C, 1)
    GPIO.output(B, 1)
    GPIO.output(A, 0)
	time.sleep(1)
	#7
    GPIO.output(D, 0)
    GPIO.output(C, 1)
    GPIO.output(B, 1)
    GPIO.output(A, 1)
	time.sleep(1)
	#8
	GPIO.output(D, 1)
    GPIO.output(C, 0)
    GPIO.output(B, 0)
    GPIO.output(A, 0)
    time.sleep(1)
	#9
	GPIO.output(D, 1)
    GPIO.output(C, 0)
    GPIO.output(B, 0)
    GPIO.output(A, 1)
    time.sleep(1)
