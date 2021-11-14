import RPi.GPIO as GPIO
import time
import paho.mqtt.client as paho
import ssl
import random
import json

def distance():        
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
    
def on_connect(client, userdata, flags, rc):  # func for making connection
    global connflag
    print("Connected to AWS")
    connflag = True
    print("Connection returned result: " + str(rc))


def on_message(client, userdata, msg):  # Func for Sending msg
    print(msg.topic + " " + str(msg.payload))


def MQTT_Message(payloadmsg1, value,
                 tag):  # For which sensor the value is, value that sensor gives, Tag for filtering the data 
    connflag = True
    mqttc = paho.Client()  # mqttc object
    mqttc.on_connect = on_connect  # assign on_connect func
    mqttc.on_message = on_message  # assign on_message func
    awshost = "a3cka59094cwjs-ats.iot.us-east-2.amazonaws.com"  # Endpoint
    awsport = 8883  # Port no.
    clientId = "SmartParkingSensor1"  # Thing_Name
    thingName = "SmartParkingSensor1"  # Thing_Name
    caPath = "/home/pi/Desktop/SmartParkingSystem/AWSCredentials/AmazonRootCA1.pem"  # Root_CA_Certificate_Name
    certPath = "/home/pi/Desktop/SmartParkingSystem/AWSCredentials" \
               "/b649e3c89e06212d62de3ca10efbc631bb30906298a17fd29f6702f6da72a446-certificate.pem.crt"  #
    # <Thing_Name>.cert.pem
    keyPath = "/home/pi/Desktop/SmartParkingSystem/AWSCredentials" \
              "/b649e3c89e06212d62de3ca10efbc631bb30906298a17fd29f6702f6da72a446-private.pem.key"  #
    # <Thing_Name>.private.key
    mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED,
                  tls_version=ssl.PROTOCOL_TLSv1_2,
                  ciphers=None)  # pass parameters
    mqttc.connect(awshost, awsport, keepalive=60)  # connect to aws server
    mqttc.loop_start()  # Start the loop
    if connflag == True:
        payloadmsgstart = "{"
        payloadmsgend = "\"}"
        payloadmsg = "{}{}{}{}".format(payloadmsgstart, payloadmsg1, value, payloadmsgend)
        payloadmsg = json.dumps(str(payloadmsg))
        payloadmsg_json1 = json.loads(payloadmsg)
        mqttc.publish(tag, payloadmsg_json1,
                      qos=1)  # topic: temperature # Publishing Temperature values
        print("msg sent")  # Print sent temperature msg on console
        print(payloadmsg_json1)
    else:
        print("waiting for connection...")

while True:
    GPIO.setmode(GPIO.BCM)#Rectangle values
    GPIO.setwarnings(False)
    GPIO_TRIG=18
    GPIO_ECHO=24
    GPIO.setup(GPIO_TRIG,GPIO.OUT)
    GPIO.setup(GPIO_ECHO,GPIO.IN)
    start_time=time.time()
    true=0
    false=0
    while time.time()-start_time<10:
        if distance():
            true+=1
        else:
            false
        time.sleep(0.1)
    if(true>false):
        MQTT_Message("\"Sensor1\":\"", True, "SmartParking/Sensor1")
    else:
        MQTT_Message("\"Sensor1\":\"", False, "SmartParking/Sensor1")


    
