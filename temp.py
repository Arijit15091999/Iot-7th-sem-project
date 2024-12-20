import csv
import time
from datetime import datetime

# File name with .csv extension
csv_file = "sensor_data.csv"

if __name__ == "__main__":
    try:
        # Create and write the header if the file doesn't exist
        with open(csv_file, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Temperature (°C)", "Humidity (%)"])
            print(f"Created new file: {csv_file}")
    except FileExistsError:
        print(f"File {csv_file} already exists. Appending new data.")

    # Example data to log
    temperature = 10
    humidity = 10

    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'Time: {timestamp}, Temp: {temperature:0.1f}°C, Humidity: {humidity:0.1f}%')

    # Write data to the CSV file
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, temperature, humidity])
        print("Data written to file.")
