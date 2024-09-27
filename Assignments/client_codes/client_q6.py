import paho.mqtt.client as mqtt
import time
import json

# MQTT broker configuration
broker_address = "test.mosquitto.org"  
broker_port = 1883  
publish_topic = "node/machine/data"  


def on_connect_callback(mqtt_client, userdata, flags, connection_result):
    print(f"Connection established, result code: {connection_result}")

mqtt_client = mqtt.Client()


mqtt_client.on_connect = on_connect_callback


mqtt_client.connect(broker_address, broker_port, 60)


mqtt_client.loop_start()

try:
    while True:
        
        sensor_data = {
            "temperature": 25.0,
            "humidity": 60.0,
            "status": "ok"
        }
        
      
        json_payload = json.dumps(sensor_data)

        mqtt_client.publish(publish_topic, json_payload)
        print(f"Published data: {json_payload}")

        time.sleep(5)

except KeyboardInterrupt:
    print("Process interrupted by user, exiting...")

finally:

    mqtt_client.loop_stop()
    mqtt_client.disconnect()