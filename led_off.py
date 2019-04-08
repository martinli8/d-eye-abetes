import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(23.GPIO.OUT)
print "LED OFF"
GPIO.output(17,GPIO.LOW)
GPIO.output(23,GPIO.LOW)
