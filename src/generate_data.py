import pandas as pd
import random

def generate_telemetry():
    data = []

    satellites = ["SAT-01", "SAT-02", "SAT-03"]

    for sat in satellites:
        for _ in range(5):
            data.append({
                "satellite_id": sat,
                "temperature": random.randint(60, 100),
                "voltage": round(random.uniform(2.7, 4.2), 2),
                "current": round(random.uniform(1.2, 3.2), 2),
                "orientation": random.randint(-70, 70)
            })

    df = pd.DataFrame(data)
    df.to_csv("../data/telemetry_data.csv", index=False)
    print("✅ Telemetry data generated")

if __name__ == "__main__":
    generate_telemetry()