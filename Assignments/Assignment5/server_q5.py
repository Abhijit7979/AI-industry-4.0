import paho.mqtt.client as mqtt
broker_address = "test.mosquitto.org"  
broker_port = 1993 
subscribe_topic = "machinedata"  


def on_message_received(client, userdata, msg):
    message_content = msg.payload.decode('utf-8')
    print(f"Message received: {message_content}")

mqtt_client = mqtt.Client()


mqtt_client.on_message = on_message_received

mqtt_client.connect(broker_address, broker_port, 60)

mqtt_client.subscribe(subscribe_topic)

mqtt_client.loop_forever()