import tkMessageBox

def counter(counterValue):

    counterValue = counterValue + 1
    print(counterValue)
    return(counterValue)
#
# def greet(self, display):
#     print("Greetings!")
#     counter = 1
#     while :
#         counter = counter +1
#         print(counter)

def exitCounter(display):
    display = False
    return display

def enterCounter(display):
    display = True;
    return display

def hello(self):
    print("Hello?")


def onClick(self,):
    tkMessageBox.showinfo("Shutdown Confirmed","Safe to power off")

# def page3_functions(self):
#     self.greet
#     self.onClick

def page3_functions(self):
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(24,GPIO.OUT)
    GPIO.setup(23.GPIO.OUT)
    print "LED OFF"
    GPIO.output(24,GPIO.LOW)
    GPIO.output(23,GPIO.LOW)
    tkMessageBox.showinfo("Shutdown Confirmed","Safe to power off")
