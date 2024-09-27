import paho.mqtt.client as mqtt
import sqlite3
import json


broker_address = "test.mosquitto.org"  
broker_port = 1883  
subscribe_topic = "node/machine/data"  


db_file = 'sensor_data.db'


def create_table():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sensor_Data (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        temperature REAL,
                        humidity REAL,
                        status TEXT,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                    )''')
    conn.commit()
    conn.close()

def insert_data(temperature, humidity, status):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sensor_data (temperature, humidity, status) VALUES (?, ?, ?)",
                   (temperature, humidity, status))
    conn.commit()
    conn.close()

def on_message_received(client, userdata, msg):
    message_content = msg.payload.decode('utf-8')
    print(f"Message received: {message_content}")

    try:
        data = json.loads(message_content)
        temperature = data.get('temperature')
        humidity = data.get('humidity')
        status = data.get('status')

        insert_data(temperature, humidity, status)
        print("Data inserted into the database.")
        
    except json.JSONDecodeError:
        print("Error decoding JSON from the message.")

mqtt_client = mqtt.Client()

mqtt_client.on_message = on_message_received

mqtt_client.connect(broker_address, broker_port, 60)

mqtt_client.subscribe(subscribe_topic)

create_table()

mqtt_client.loop_forever()
