import RPi.GPIO as GPIO
import time
import random
import pyrebase

config={
    "apiKey": "AIzaSyAZYM5i0zhsjxB9uUoWsFEL28VSpxsoTIo",
  "authDomain": "smartparkingsensor-group7.firebaseapp.com",
  "databaseURL": "https://smartparkingsensor-group7-default-rtdb.firebaseio.com",
  "projectId": "smartparkingsensor-group7",
  "storageBucket": "smartparkingsensor-group7.appspot.com",
  "messagingSenderId": "810478901892",
  "appId": "1:810478901892:web:abffb8aa6ec2f98729c0d1",
  "measurementId": "G-G4D2SXJ92Z"
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
    print(value)
    data={databaseName:value}
    database.set(data)
    

while True:
    GPIO.setmode(GPIO.BCM)#Rectangle values
    GPIO.setwarnings(False)
    GPIO_TRIG1=14
    GPIO_ECHO1=15
    GPIO_TRIG2=20
    GPIO_ECHO2=21
    GPIO_TRIG3=2
    GPIO_ECHO3=3
    GPIO.setup(GPIO_TRIG1,GPIO.OUT)
    GPIO.setup(GPIO_ECHO1,GPIO.IN)
    start_time=time.time()
    true=0
    false=0
    while time.time()-start_time<3:
        if distance(GPIO_TRIG1,GPIO_ECHO1)==True:
            true+=1
        else:
            false+=1
        time.sleep(0.1)
    if(true>=false):
        firebaseSender("Sensor1",True)
    else:
        firebaseSender("Sensor1",False)
    
    GPIO.setup(GPIO_TRIG2,GPIO.OUT)
    GPIO.setup(GPIO_ECHO2,GPIO.IN)
    start_time=time.time()
    true=0
    false=0
    while time.time()-start_time<3:
        if distance(GPIO_TRIG2,GPIO_ECHO2)==True:
            true+=1
        else:
            false+=1
        time.sleep(0.1)
    if(true>=false):
        firebaseSender("Sensor2",True)
    else:
        firebaseSender("Sensor2",False)
        
    GPIO.setup(GPIO_TRIG3,GPIO.OUT)
    GPIO.setup(GPIO_ECHO3,GPIO.IN)
    start_time=time.time()
    true=0
    false=0
    while time.time()-start_time<3:
        if distance(GPIO_TRIG3,GPIO_ECHO3)==True:
            true+=1
        else:
            false+=1
        time.sleep(0.1)
    if(true>=false):
        firebaseSender("Sensor3",True)
    else:
        firebaseSender("Sensor3",False)



    

