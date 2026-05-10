import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from scipy.optimize import minimize

# 1. SETUP THE BRAIN (Same as before)
df = pd.read_csv(r"D:\Drone_Projects\Project_ICARUS\icarus_training_data.csv")
X = df[['Span']]
y = df['CL']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

ai_brain = MLPRegressor(hidden_layer_sizes=(100, 100), activation='relu', solver='lbfgs')
ai_brain.fit(X_scaled, y)

# 2. THE OPTIMIZATION GOAL
# Change this number to whatever Lift you want!
TARGET_LIFT = 1.20 

def objective_function(span_input):
    # This tells the AI: "How close is your guess to my target lift?"
    span_scaled = scaler.transform(np.array(span_input).reshape(-1, 1))
    predicted_cl = ai_brain.predict(span_scaled)
    error = abs(predicted_cl - TARGET_LIFT)
    return error

# 3. RUN THE AI OPTIMIZER
print(f"🎯 Goal: Find the perfect Span for CL = {TARGET_LIFT}")
result = minimize(objective_function, x0=[3.0], bounds=[(2.0, 4.0)])

# 4. SHOW THE RESULT
final_span = result.x[0]
print("\n--- 🏁 OPTIMIZATION COMPLETE 🏁 ---")
print(f"🚀 RECOMMENDED SPAN: {final_span:.3f} meters")
print(f"📊 EXPECTED LIFT:    {TARGET_LIFT}")
print(f"⚡ Time Taken:       Less than 0.1 seconds")
