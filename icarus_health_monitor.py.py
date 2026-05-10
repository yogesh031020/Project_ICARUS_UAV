import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
# 1. LOAD THE SENSOR DATA
data = pd.read_csv(r"D:\Drone_Projects\Project_ICARUS\icarus_health_data.csv")
X = data[['Speed', 'Vibration_Hz']]
y = data['Health_Status']
# 2. TRAIN THE "STRUCTURAL DOCTOR"
print("🩺 AI is learning Wing Fatigue Patterns...")
health_ai = RandomForestClassifier(n_estimators=100)
health_ai.fit(X, y)
# 3. TEST A SCENARIO
# Flying at 35 m/s with 55Hz vibration
test_scenario = [[35, 55]]
prediction = health_ai.predict(test_scenario)
if prediction[0] == 1:
    print("\n🚨 WARNING: CRITICAL FLUTTER DETECTED! Wing failure imminent!")
else:
    print("\n✅ STATUS: Structural Integrity Optimal.")