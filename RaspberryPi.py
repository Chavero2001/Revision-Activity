import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO # General Purpose Input/Output library

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)

led_pin = 2

GPIO.setup(led_pin, GPIO.OUT)

# Define the MQTT broker and topic
broker_address = "localhost"  # Replace with the Raspberry Pi's IP if not running locally
topic = "room/lighting"  # Replace with the desired MQTT topic

# Callback functions for MQTT client
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, message):
    print(f"Received message on topic '{message.topic}': {message.payload.decode()}")
    room_light=int(message.payload.decode())
    set_point=3000
    if room_light>3000:
         GPIO.output(led_pin, 1)
    else:
        GPIO.output(led_pin, 0)
        
# Create an MQTT client
client = mqtt.Client()

# Set up callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address)

# Start the MQTT client loop to receive messages
client.loop_forever()
