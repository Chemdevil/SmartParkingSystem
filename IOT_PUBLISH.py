# importing libraries
import paho.mqtt.client as paho
import ssl
import random
import json


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
    awshost = ""  # Endpoint
    awsport =   # Port no.
    clientId = ""  # Thing_Name
    thingName = ""  # Thing_Name
    caPath = ""  # Root_CA_Certificate_Name
    certPath = ""  # <Thing_Name>.cert.pem
    keyPath = ""   # <Thing_Name>.private.key
    mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED,
                  tls_version=ssl.PROTOCOL_TLSv1_2,
                  ciphers=None)  # pass parameters
    mqttc.connect(awshost, awsport, keepalive=60)  # connect to aws server
    mqttc.loop_start()  # Start the loop
    if connflag == True:
        payloadmsgstart = "{"
        payloadmsgend = "\"}"
        payloadmsg = "{} {} {} {}".format(payloadmsgstart, payloadmsg1, value, payloadmsgend)
        payloadmsg = json.dumps(str(payloadmsg))
        payloadmsg_json1 = json.loads(payloadmsg)
        mqttc.publish(tag, payloadmsg_json1,
                      qos=1)  # topic: temperature # Publishing Temperature values
        print("msg sent")  # Print sent temperature msg on console
        print(payloadmsg_json1)
    else:
        print("waiting for connection...")


i = 100
while i != 0:
    MQTT_Message("\"Sensor1\":\"", random.choice([True, False]), "SmartParking/Sensor1")
    MQTT_Message("\"Sensor2\":\"", random.choice([True, False]), "SmartParking/Sensor2")
    MQTT_Message("\"Sensor3\":\"", random.choice([True, False]), "SmartParking/Sensor3")
    i = i - 1
