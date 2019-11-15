import paho.mqtt.client as mqtt
MQTT_SERVER = "192.168.43.147"
MQTT_PATH = "ee180d/test"

# The callback for when the client receives a connect response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # on_connect() means that if we lose the connection and reconnect then subs$
    client.subscribe(MQTT_PATH)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
   # print(msg.topic + " string: " + str(msg.payload))
    print(" string: " + str(msg.payload))
    if str(msg.payload) == "b'a'":
        print("received yes signal")
    # more callbacks, etc

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
