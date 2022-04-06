import pyrebase
import random

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
