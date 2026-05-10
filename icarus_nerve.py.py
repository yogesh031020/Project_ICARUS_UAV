from pymavlink import mavutil
import time
print("🕵️‍♂️ Starting Raw MAVLink Spy...")
connection = mavutil.mavlink_connection('tcp:127.0.0.1:5762')
# Wait for heartbeat
connection.wait_heartbeat()
print("✅ CONNECTION LIVE")
# Request everything
connection.mav.request_data_stream_send(connection.target_system, connection.target_component,
                                        mavutil.mavlink.MAV_DATA_STREAM_ALL, 1, 1)
print("📡 LISTENING TO RAW STREAM (5 seconds)...")
start_time = time.time()
while time.time() - start_time < 5:
    msg = connection.recv_match(blocking=True)
    if msg:
        print(f"📦 Received: {msg.get_type()}")
print("\n--- TEST FINISHED ---")