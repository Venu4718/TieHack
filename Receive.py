import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
p = GPIO.PWM(7,50)
p.start(2.5)
rmsg = ""
broker = "10.0.10.97"

def servo():
        try:
                p.ChangeDutyCycle(7.5)
                time.sleep(1)
                p.ChangeDutyCycle(2.5)
        except KeyboardInterrupt:
                p.stop()
                GPIO.cleanup()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("pi")


def on_message(client, userdata, msg):
    print "message"
    print(msg.topic+" "+str(msg.payload.decode("utf-8")))
    rmsg = msg.payload.decode("utf-8")
    if str(rmsg) == "on":
                print "servo roate"
                servo()
client = mqtt.Client("c")
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker)
client.loop_forever()
   