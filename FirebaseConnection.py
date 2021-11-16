import pyrebase
import random

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

def firebaseSender(databaseName,value):
    firebase=pyrebase.initialize_app(config)
    storage=firebase.storage()
    database=firebase.database()
    database.child(databaseName)
    data={"Sensor1":value}
    database.set(data)
    
i=50    
while i!=0:
    firebaseSender("Sensor1",random.choice([True,False]))
    firebaseSender("Sensor2",random.choice([True,False]))
    firebaseSender("Sensor3",random.choice([True,False]))
    print(i)
    i=i-2