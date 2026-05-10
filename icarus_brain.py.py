import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 1. LOAD DATA
df = pd.read_csv(r"D:\Drone_Projects\Project_ICARUS\icarus_training_data.csv")
X = df[['Span']]
y = df['CL']

# 2. THE SECRET TRICK: SCALING
# This makes the data "Friendly" for the Neural Network
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. THE HIGH-POWERED BRAIN
print("🧠 Training the High-Precision Brain...")
ai_brain = MLPRegressor(
    hidden_layer_sizes=(100, 100), 
    activation='relu', 
    solver='lbfgs', # Changed to LBFGS for small datasets (it is much more accurate)
    max_iter=10000
)

# 4. TRAIN
ai_brain.fit(X_scaled, y)
print("✅ AI HAS MASTERED AERODYNAMICS!")

# 5. PREDICT & VISUALIZE
x_range = np.linspace(2.0, 4.0, 100).reshape(-1, 1)
x_range_scaled = scaler.transform(x_range)
predictions = ai_brain.predict(x_range_scaled)

plt.figure(figsize=(10,6))
plt.scatter(X, y, color='blue', alpha=0.5, label='Real Physics Data')
plt.plot(x_range, predictions, color='red', linewidth=3, label='AI Understanding')
plt.title("Project ICARUS 2.0: AI-Powered Aerodynamic Model")
plt.xlabel("Wing Span (m)")
plt.ylabel("Lift Coefficient (CL)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()
