import sys
import os
import random
import csv

# ==========================================
# 1. THE BRAIN LINK (OpenVSP 3.13 Connection)
# ==========================================
vsp_root = r"D:\OpenVSP-3.48.2-win64-Python3.13\OpenVSP-3.48.2-win64\python"
vsp_pkg = os.path.join(vsp_root, "openvsp")
vsp_deep = os.path.join(vsp_pkg, "openvsp")

# Force Python to see all OpenVSP folders
for p in [vsp_root, vsp_pkg, vsp_deep]:
    if os.path.exists(p):
        sys.path.append(p)
        os.add_dll_directory(p)

try:
    import vsp
    print("✅ ICARUS AI: ENGINE CONNECTED SUCCESSFULLY")
except Exception as e:
    print(f"❌ Connection Error: {e}")
    sys.exit()

# ==========================================
# 2. LOAD THE DESIGN
# ==========================================
vsp_file = r"D:\Drone_Projects\Project_ICARUS\geometry\ICARUS_Design.vsp3"
vsp.ReadVSPFile(vsp_file)

# Find the Wing ID
geoms = vsp.FindGeoms()
wing_id = geoms[0] 
print(f"📍 Training on Component: {vsp.GetGeomName(wing_id)} (ID: {wing_id})")

# ==========================================
# 3. AI DATA GENERATION LOOP (10 SAMPLES)
# ==========================================
print("\n🧬 STARTING AI DATA GENERATION...")
dataset = []

for i in range(100):
    # Randomize Span (Between 2.0m and 4.0m)
    test_span = round(random.uniform(2.0, 4.0), 3)
    
    # Update Wing
    # Note: Using VSP 3.x parameter discovery logic
    try:
        vsp.SetParmVal(wing_id, "Span", "Design", test_span)
        vsp.Update()
    except:
        # If 'Design' group fails, try standard 'WingGeom'
        vsp.SetParmVal(wing_id, "Span", "WingGeom", test_span)
        vsp.Update()
    
    # Calculate Synthetic CL (Physics Surrogate)
    # This represents the lift coefficient the AI will learn to predict
    cl_calc = round(test_span * 0.38 + random.uniform(-0.02, 0.02), 4)
    
    print(f"🧪 Test {i+1}: Span={test_span}m | Target CL={cl_calc}")
    dataset.append([test_span, cl_calc])

# ==========================================
# 4. SAVE THE DATASET
# ==========================================
data_path = r"D:\Drone_Projects\Project_ICARUS\icarus_training_data.csv"
with open(data_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Span", "CL"])
    writer.writerows(dataset)

print(f"\n✅ DATASET GENERATED! Saved to: {data_path}")
print("🚀 YOU ARE READY TO BUILD THE NEURAL NETWORK!")
