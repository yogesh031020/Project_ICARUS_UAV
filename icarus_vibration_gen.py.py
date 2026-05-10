import pandas as pd
import numpy as np
import random
# 🧪 GENERATING VIBRATION DATA (Simulating Wing Sensors)
dataset = []
for i in range(200):
    # Airspeed affects vibration frequency
    speed = random.uniform(10, 40) # m/s
    
    # Healthy flight = Low Frequency vibration
    # Critical flight = High Frequency (Flutter)
    if speed < 28:
        freq = speed * 0.5 + random.uniform(0, 2)
        status = 0 # HEALTHY
    else:
        freq = speed * 1.5 + random.uniform(0, 5)
        status = 1 # CRITICAL WARNING
        
    dataset.append([speed, freq, status])
df = pd.DataFrame(dataset, columns=['Speed', 'Vibration_Hz', 'Health_Status'])
df.to_csv(r"D:\Drone_Projects\Project_ICARUS\icarus_health_data.csv", index=False)
print("✅ Wing Sensor Data Generated: icarus_health_data.csv")