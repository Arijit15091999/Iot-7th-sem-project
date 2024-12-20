import Adafruit_DHT
import time
from datetime import datetime
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_DATABASE = os.getenv("MONGO_DATABASE")
MONGO_URI_TEMPLATE = "mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@cluster0.zuwtmhg.mongodb.net/{MONGO_DATABASE}"
MONGO_URI = MONGO_URI_TEMPLATE.format(
    MONGO_USER=MONGO_USER,
    MONGO_PASSWORD=MONGO_PASSWORD,
    MONGO_DATABASE=MONGO_DATABASE
)

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[MONGO_DATABASE]
collection = db["dht11_sensor_data"]  # Updated collection name

# Sensor and GPIO setup
sensor = Adafruit_DHT.DHT11
pin = 21

print("Recording data to MongoDB... Press Ctrl+C to stop.")

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            timestamp = datetime.now()
            print(f'Time: {timestamp}, Temp: {temperature:0.1f}°C, Humidity: {humidity:0.1f}%')
            
            # Insert data into MongoDB
            document = {
                "sensor_type": "DHT11",
                "pin": pin,
                "timestamp": timestamp,
                "temperature": round(temperature, 1),
                "humidity": round(humidity, 1)
            }
            collection.insert_one(document)
        else:
            print('Failed to get reading. Try again!')
        time.sleep(1)

except KeyboardInterrupt:
    print("\nData recording to MongoDB stopped.")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    client.close()
