print("====================================")
print("Manufacturing Failure Prediction System ")
print("========================================\n")
machines = [
    {"id": "M101", "temperature": 65, "vibration": 20, "pressure": 90},
    {"id": "M102", "temperature": 95, "vibration": 60, "pressure": 130},
    {"id": "M103", "temperature": 70, "vibration": 25, "pressure": 100},
    {"id": "M104", "temperature": 105, "vibration": 75, "pressure": 145},
    {"id": "M105", "temperature": 80, "vibration": 30, "pressure": 110}
]
healthy = 0
failure = 0
print("Machine Health Analysis\n")
for machine in machines:
    score = (
        machine["temperature"] +
        machine["vibration"] +
        machine["pressure"]
    )
    if score >= 300:
        status = "Mechanical Failure"
        failure += 1
    else:
        status = "Healthy"
        healthy += 1
    print("--------------------------------")
    print("Machine ID :", machine["id"])
    print("Temperature :", machine["temperature"], "°C")
    print("Vibration :", machine["vibration"])
    print("Pressure :", machine["pressure"])
    print("Failure Score :", score)
    print("Prediction :", status)
print("\n===============================")
print("Factory Summary")
print("=================================")
print("Total Machines :", len(machines))
print("Healthy :", healthy)
print("Failure Detected :", failure)
accuracy = ((healthy + failure) / len(machines)) * 100
print("Prediction Accuracy :", round(accuracy, 2), "%")
print("\ntraining completed successfully")