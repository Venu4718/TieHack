import RPi.GPIO as GPIO
import MFRC522
import signal
import paho.mqtt.client as paho
userID = []
continue_reading = True
broker ="10.0.10.97"
client = paho.Client("cl1")
client.connect(broker)
client.loop_start()
client.subscribe("pi")

def on_message(client,userdata,mesage):
        print("message receved",str(message.payload.decode("utf-8")))

client.on_message = on_message
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

signal.signal(signal.SIGINT, end_read)


MIFAREReader = MFRC522.MFRC522()


print "Welcome to the MFRC522 data read example"
print "Press Ctrl-C to stop."


while continue_reading:
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    if status == MIFAREReader.MI_OK:
        print "Card detected"


    (status,uid) = MIFAREReader.MFRC522_Anticoll()
    if status == MIFAREReader.MI_OK:

        # print "Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3])
        if ((uid[0] in userID) and ((uid[0]==11) or (uid[0]==19))):
            client.subscribe("user")
            client.publish("user",str(uid[0]))
            userID.append(uid[0])
        else:

            client.subscribe("travel")
            client.publish("travel",str(uid[0]))
            if uid[0] in userID:
                        userID.remove(uid[0])
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]


        MIFAREReader.MFRC522_SelectTag(uid)


        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key,ui$


        if status == MIFAREReader.MI_OK:
            MIFAREReader.MFRC522_Read(8)
            MIFAREReader.MFRC522_StopCrypto1()
        else:
            print "Authentication error"

