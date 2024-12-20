import time
from datetime import datetime
from max30100 import MAX30100
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
collection = db["spo2_pulse_data"]  # Updated collection name

# Sensor setup
mx30 = MAX30100()
mx30.enable_spo2()

print("Recording SpO2 and pulse data to MongoDB... Press Ctrl+C to stop.")

try:
    while True:
        mx30.read_sensor()

        ir_value = mx30.ir
        red_value = mx30.red

        # Calculate pulse and SpO2 values
        hb = int(ir_value / 100) if ir_value else 0
        spo2 = int(red_value / 100) if red_value else 0

        timestamp = datetime.now()

        if ir_value:
            print(f"Time: {timestamp}, Pulse: {hb} bpm, SpO2: {spo2}%")

            # Insert data into MongoDB
            document = {
                "timestamp": timestamp,
                "pulse_bpm": hb,
                "spo2_percent": spo2,
                "sensor_type": "MAX30100"
            }
            collection.insert_one(document)

        time.sleep(2)

except KeyboardInterrupt:
    print("\nMonitoring stopped.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Shutting down sensor...")
    client.close()
