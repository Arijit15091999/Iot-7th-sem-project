import Adafruit_DHT
import time
import csv
from datetime import datetime

# Sensor and GPIO setup
sensor = Adafruit_DHT.DHT11
pin = 21

csv_file = f"sensor_dht11_pin_{pin}.csv"

try:
    with open(csv_file, mode='x', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Temperature (°C)", "Humidity (%)"])
except FileExistsError:
    print(f"{csv_file} already exists. New data will be appended.")

print(f"Recording data to {csv_file}... Press Ctrl+C to stop.")

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f'Time: {timestamp}, Temp: {temperature:0.1f}°C, Humidity: {humidity:0.1f}%')
            
            with open(csv_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([timestamp, temperature, humidity])
        else:
            print('Failed to get reading. Try again!')
        time.sleep(1)

except KeyboardInterrupt:
    print(f"\nData recording to {csv_file} stopped.")
