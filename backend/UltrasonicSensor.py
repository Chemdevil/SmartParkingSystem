import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)#Rectangle values
GPIO.setwarnings(False)
GPIO_TRIG=18
GPIO_ECHO=24
def distance():    
    GPIO.setup(GPIO_TRIG,GPIO.OUT)
    GPIO.setup(GPIO_ECHO,GPIO.IN)
    GPIO.output(GPIO_TRIG,True)
    time.sleep(0.0001)
    GPIO.output(GPIO_TRIG,False)
    start_time=time.time()
    return_time=time.time()
    while GPIO.input(GPIO_ECHO)==0:
        start_time=time.time()
    while GPIO.input(GPIO_ECHO)==1:
        return_time=time.time()
    distance=((return_time-start_time)*34300)/2
    if(distance<30):#Ground clearance
        print(distance,"cm")
        return True
    else:
        return False

while True:
    print(distance())
    time.sleep(0.1)
    