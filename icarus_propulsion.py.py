import pandas as pd

# 1. ICARUS SPECIFICATIONS
mtow = 8.0  # kg
target_thrust_total = mtow * 2.0 # 2:1 Ratio

print(f"🚁 ICARUS MTOW: {mtow} kg")
print(f"⚡ Target Thrust: {target_thrust_total} kg")

# 2. MOTOR/PROP DATABASE (Sample Data)
motors = [
    {"Name": "T-Motor U8 Lite", "KV": 150, "MaxThrust_kg": 5.2, "Weight_g": 240},
    {"Name": "T-Motor MN605-S", "KV": 170, "MaxThrust_kg": 4.1, "Weight_g": 180},
    {"Name": "Standard 5010", "KV": 360, "MaxThrust_kg": 2.5, "Weight_g": 120}
]

# 3. SELECTION LOGIC
print("\n--- 🔍 Propulsion Match Analysis ---")
for motor in motors:
    # Assume 4 motors (Quad-Plane or Twin-Motor setup)
    num_motors = 2 # Twin motor for HALE
    total_max = motor["MaxThrust_kg"] * num_motors
    
    if total_max >= target_thrust_total:
        status = "✅ CAPABLE"
    else:
        status = "❌ UNDERPOWERED"
        
    print(f"Motor: {motor['Name']} | Max Thrust: {total_max:.1f}kg | Status: {status}")

print("\n💡 Recommendation: For a 3.16m HALE UAV, we should use Twin T-Motor U8 Lite motors with 28-inch props.")

# 4. ENDURANCE CALCULATION
battery_capacity_ah = 30.0 # Huge 30Ah LiPo
voltage = 22.2 # 6S Battery
cruise_amp_draw = 12.0 # Estimated Amps needed to stay level at 3.16m span

# Formula: (Capacity / Amp Draw) * 60 minutes
flight_time_minutes = (battery_capacity_ah / cruise_amp_draw) * 60

print(f"\n--- ⏳ ENDURANCE REPORT ---")
print(f"🔋 Battery: {battery_capacity_ah}Ah (6S)")
print(f"⏱️ Estimated Flight Time: {flight_time_minutes:.1f} Minutes ({flight_time_minutes/60:.1f} Hours)")
print(f"🌍 Range at 60km/h: {flight_time_minutes/60 * 60:.1f} km")
