import time
import csv
from datetime import datetime
from max30100 import MAX30100

mx30 = MAX30100()
mx30.enable_spo2()

csv_file = "spo2_pulse_data.csv"

try:
    with open(csv_file, mode='x', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Pulse (bpm)", "SpO2 (%)"])
        print(f"Created new file: {csv_file}")
except FileExistsError:
    print(f"File {csv_file} already exists. Appending new data.")

try:
    while True:
        mx30.read_sensor()

        ir_value = mx30.ir
        red_value = mx30.red

        hb = int(ir_value / 100) if ir_value else 0
        spo2 = int(red_value / 100) if red_value else 0

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if ir_value:
            print(f"Time: {timestamp}, Pulse: {hb} bpm, SpO2: {spo2}%")

        with open(csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, hb, spo2])

        time.sleep(2)

except KeyboardInterrupt:
    print("\nMonitoring stopped.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Shutting down sensor...")
