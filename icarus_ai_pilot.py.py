from pymavlink import mavutil
import time
# 1. CONNECT
print("📡 Connecting AI Pilot to ICARUS...")
connection = mavutil.mavlink_connection('tcp:127.0.0.1:5762')
connection.wait_heartbeat()
print("✅ AI PILOT ONLINE")
TARGET_ALT = 100.0 
def set_elevator(pwm_value):
    # Channel 2 is Elevator
    connection.mav.rc_channels_override_send(
        connection.target_system, connection.target_component,
        65535, pwm_value, 65535, 65535, 65535, 65535, 65535, 65535
    )
print("\n🚀 STARTING AUTONOMOUS ALTITUDE HOLD...")
try:
    while True:
        # Get Current Altitude
        msg = connection.recv_match(type='VFR_HUD', blocking=True)
        current_alt = msg.alt
        
        # AI LOGIC
        error = TARGET_ALT - current_alt
        
        if error > 2: # Too low! Need to Climb
            action = 1650 # PULL UP
            status = "🔼 CLIMBING"
        elif error < -2: # Too high! Need to Dive
            action = 1350 # PUSH DOWN
            status = "🔽 DIVING"
        else:
            action = 1500 # Neutral
            status = "↔️ LEVEL"
            
        set_elevator(action)
        print(f"🛰️ Alt: {current_alt:.1f}m | Status: {status} | Action: {action}")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("🛑 AI Pilot shutting down.")
    set_elevator(1500)