import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(23.GPIO.OUT)
print "LED on"
GPIO.output(24,GPIO.HIGH)
GPIO.output(23,GPIO.HIGH)
