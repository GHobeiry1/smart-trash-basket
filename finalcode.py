import pibrella
from time import sleep
import time
import RPi.GPIO as GPIO

# Pin Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Motor 1
M1_E = 13 
M1_IN1 = 19
M1_IN2 = 26
GPIO.setup(M1_E, GPIO.OUT)
GPIO.setup(M1_IN1, GPIO.OUT)
GPIO.setup(M1_IN2, GPIO.OUT)
motor1 = GPIO.PWM(M1_E, 50)



def opendoor():
    """Runs motor forward"""

    GPIO.output(M1_IN1, False)
    GPIO.output(M1_IN2, True)
    

def closedoor():
    """Runs motor backwards"""
    GPIO.output(M1_IN2, False)
    GPIO.output(M1_IN1, True)

def drop():
    print 'Droping Trash'
    # Start  motors
    motor1.start(100)

    # Go forward for 1 seconds
    opendoor()
    time.sleep(1)
    
    # stop motor for 5 seconds
    motor1.stop()
    time.sleep(2)
    motor1.start(100)
    motor1.ChangeDutyCycle(90)

    # Go backwards for 1 seconds
    closedoor()
    time.sleep(1)
    motor1.stop()










def rotateM():
    pibrella.light.red.on()
    forward(450,0.005)
    sleep(1)
    drop()
    backward(450,0.005)
    pibrella.light.red.off()
    pibrella.buzzer.success()   
        
def rotateC():
    pibrella.light.green.on()
    forward(950,0.005)
    sleep(1)
    drop()
    backward(950,0.005)
    pibrella.light.green.off()
    pibrella.buzzer.success()
    
def forward(steps,delay):           
             pibrella.output.e.off()
             pibrella.output.f.on()
             count = 0
             while (count <= steps):
                            pibrella.output.g.on()
                            sleep(delay)
                            pibrella.output.g.off()
                            count = count + 1

def backward(steps,delay):
            pibrella.output.e.off()
            pibrella.output.f.off()
            count = 0
            while (count <= steps):
                            pibrella.output.g.on()
                            sleep(delay)
                            pibrella.output.g.off()
                            count = count + 1


try:
    while True:
        Metal = pibrella.input.b.read()
        Paper = pibrella.input.a.read()
        sleep(2)
        motion = pibrella.input.c.read()
        # Check for input b
        if Metal == 0:
            print 'Metal detected'
            rotateM()
            
        # Check for input a
        elif Paper == 0:
                print 'Paper or plastic detected'
                rotateC()
       # Check for input a,b,c
        elif motion == 0:
            print 'Glass detected'
            drop()

                    
except KeyboardInterrupt:
    print 'Interrupted'
