import RPi.GPIO as GPIO
import time
import random
import pyrebase

config={
    "apiKey": "",
  "authDomain": "",
  "databaseURL": "",
  "projectId": "",
  "storageBucket": "",
  "messagingSenderId": "",
  "appId": "",
  "measurementId": ""
    };

def distance(GPIO_TRIG,GPIO_ECHO):        
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
        return True
    else:
        return False
    
def firebaseSender(databaseName,value):
    firebase=pyrebase.initialize_app(config)
    storage=firebase.storage()
    database=firebase.database()
    database.child(databaseName)
    print(databaseName,value)
    data={databaseName:value}
    database.set(data)

def helper_function(GPIO_TRIG,GPIO_ECHO,SensorName):
    GPIO.setup(GPIO_TRIG,GPIO.OUT)
    GPIO.setup(GPIO_ECHO,GPIO.IN)
    start_time=time.time()
    true=0
    false=0
    while time.time()-start_time<3:
        if distance(GPIO_TRIG,GPIO_ECHO)==True:
            true+=1
        else:
            false+=1
        time.sleep(0.1)
    if(true>=false):
        firebaseSender(SensorName,True)
    else:
        firebaseSender(SensorName,False)
        
        
while True:
    GPIO.setmode(GPIO.BCM)#Rectangle values
    GPIO.setwarnings(False)
    GPIO_TRIG1=14
    GPIO_ECHO1=15
    GPIO_TRIG2=20
    GPIO_ECHO2=21
    GPIO_TRIG3=2
    GPIO_ECHO3=3
    helper_function(GPIO_TRIG1,GPIO_ECHO1,"Sensor1")
    helper_function(GPIO_TRIG2,GPIO_ECHO2,"Sensor2")
    helper_function(GPIO_TRIG3,GPIO_ECHO3,"Sensor3")


