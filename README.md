# 🦅 Project ICARUS 2.0: AI-Driven HALE UAV Design
**An Intelligent Engineering System for High-Altitude Long-Endurance (HALE) Autonomy.**
## 🚀 Project Overview
Project ICARUS is a complete end-to-end aerospace engineering pipeline that transitions from high-fidelity structural certification to AI-driven design optimization and autonomous flight.
## 🛠️ Key Achievements
### 1. Structural Certification (FEA)
- **Software:** PrePoMax / CalculiX.
- **Result:** Successfully certified a 3.0m Carbon Fiber airframe under 211N static load (Max Stress: 9.77e4 Pa).
### 2. AI Design Optimization (Path A)
- **Algorithm:** Multi-Layer Perceptron (MLP) Neural Network.
- **Optimization:** Programmatically evolved the wing span from 3.0m to **3.16m** to achieve a target Lift Coefficient (CL) of 1.2.
### 3. Autonomous Avionics (SITL)
- **Environment:** ArduPilot Mission Planner SITL.
- **Milestone:** Executed a fully autonomous waypoint mission with HALE-optimized flight parameters.
### 4. Intelligence Phase (Path B & C)
- **AI Pilot (RL):** Implemented a Python-Mavlink bridge for real-time neural attitude control.
- **Digital Twin (Health):** Developed a Random Forest classifier to predict **Critical Wing Flutter** and prevent structural failure.
## 📂 Repository Structure
- `/geometry`: OpenVSP (.vsp3) airframe models.
- `/ai`: Python scripts for optimization and health monitoring.
- `/results`: FEA stress maps, AI learning curves, and SITL flight logs.
- `/data`: Synthetic aerodynamic datasets generated via API.
## 👨‍💻 Developed By
**Yogesh E S**
*Aerospace AI & Drone Autonomy Engineer*