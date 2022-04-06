# importing libraries
import paho.mqtt.client as paho
import os
import socket
import ssl
import random
import string
import json
from time import sleep
from random import uniform
 
connflag = False
 
def on_connect(client, userdata, flags, rc):                # func for making connection
    global connflag
    print ("Connected to AWS")
    connflag = True
    print("Connection returned result: " + str(rc) )
 
def on_message(client, userdata, msg):                      # Func for Sending msg
    print(msg.topic+" "+str(msg.payload))
    
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
    return result_str
    
def getMAC(interface='eth0'):
  # Return the MAC address of the specified interface
  try:
    str = open('/sys/class/net/%s/address' %interface).read()
  except:
    str = "00:00:00:00:00:00"
  return str[0:17]
def getEthName():
  # Get name of the Ethernet interface
  try:
    for root,dirs,files in os.walk('/sys/class/net'):
      for dir in dirs:
        if dir[:3]=='enx' or dir[:3]=='eth':
          interface=dir
  except:
    interface="None"
  return interface
 
#def on_log(client, userdata, level, buf):
#    print(msg.topic+" "+str(msg.payload))
 
mqttc = paho.Client()                                       # mqttc object
mqttc.on_connect = on_connect                               # assign on_connect func
mqttc.on_message = on_message                               # assign on_message func
#mqttc.on_log = on_log

#### Change following parameters #### 
awshost = ""      # Endpoint
awsport =                                               # Port no.   
clientId = ""                                     # Thing_Name
thingName = ""                                    # Thing_Name
caPath = ""                                      # Root_CA_Certificate_Name
certPath = ""                            # <Thing_Name>.cert.pem
keyPath = ""                          # <Thing_Name>.private.key
 
mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)  # pass parameters
 
mqttc.connect(awshost, awsport, keepalive=60)               # connect to aws server
 
mqttc.loop_start()                                          # Start the loop
 
while 1==1:
    sleep(5)
    if connflag == True:
        #ethName=getEthName()
        #ethMAC=getMAC(ethName)
        #macIdStr = ethMAC
        #randomNumber = uniform(20.0,25.0)
        #random_string= get_random_string(8)
        payloadmsgstart="{"
        payloadmsg1="\"Sensor1\":\""
        payloadmsg2="\"Sensor2\":\""
        payloadmsg3="\"Sensor3\":\""
        payloadmsgend="\"}"
        payloadmsg1="{} {} {} {}".format(payloadmsgstart,payloadmsg1,random.choice([True,False]),payloadmsgend)
        payloadmsg1 = json.dumps(str(payloadmsg1)) 
        payloadmsg_json1 = json.loads(payloadmsg1)
        
        payloadmsg2="{} {} {} {}".format(payloadmsgstart,payloadmsg2,random.choice([True,False]),payloadmsgend)
        payloadmsg2 = json.dumps(str(payloadmsg2)) 
        payloadmsg_json2 = json.loads(payloadmsg2)
        
        payloadmsg3="{} {} {} {}".format(payloadmsgstart,payloadmsg3,random.choice([True,False]),payloadmsgend)
        payloadmsg3 = json.dumps(str(payloadmsg3)) 
        payloadmsg_json3 = json.loads(payloadmsg3)
        
        mqttc.publish("SmartParking/Sensor1", payloadmsg_json1 , qos=1)        # topic: temperature # Publishing Temperature values
        mqttc.publish("SmartParking/Sensor2", payloadmsg_json2 , qos=1)
        mqttc.publish("SmartParking/Sensor3", payloadmsg_json3 , qos=1)
        print("msg sent" ) # Print sent temperature msg on console
        print(payloadmsg_json1)
        print(payloadmsg_json2)
        print(payloadmsg_json3)
        

    else:
        print("waiting for connection...")                      
