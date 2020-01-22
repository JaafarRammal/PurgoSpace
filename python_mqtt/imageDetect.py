#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import base64
from PIL import Image
import io

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("image")

def on_message(client, userdata, msg):
  print("Received message")
  imgdata = base64.b64decode(msg.payload.decode())
  filename = 'output.jpg'
  with open(filename, 'wb') as f:
    f.write(imgdata)
    
client = mqtt.Client()
client.connect("172.20.10.11",1234,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()