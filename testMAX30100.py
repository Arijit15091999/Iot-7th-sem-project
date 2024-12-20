import time
import csv
from datetime import datetime

import max30100

mx30 = max30100.MAX30100()
mx30.enable_spo2()

csv_file = "spo2_pluse_data.csv"

try:
    # Create and write the header if the file doesn't exist
    with open(csv_file, mode='x', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Temperature (°C)", "Humidity (%)"])
        print(f"Created new file: {csv_file}")
except FileExistsError:
    print(f"File {csv_file} already exists. Appending new data.")


while 1:
    mx30.read_sensor()

    mx30.ir, mx30.red

    hb = int(mx30.ir / 100)
    spo2 = int(mx30.red / 100)


    
    if mx30.ir != mx30.buffer_ir :
        print("Pulse:",hb);
    if mx30.red != mx30.buffer_red:
        print("SPO2:",spo2);

    time.sleep(2)       