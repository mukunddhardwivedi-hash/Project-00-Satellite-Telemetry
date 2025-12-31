import pandas as pd
from anomaly_detector import rule_based_detection
from ml_anomaly_detector import apply_ml_detection
from generate_data import generate_telemetry

print("🚀 PROJECT 00 – SATELLITE ANOMALY REPORT")

# Generate telemetry automatically
generate_telemetry()

# Load data
df = pd.read_csv("../data/telemetry_data.csv")

# Rule-based detection
df["rule_anomalies"] = df.apply(rule_based_detection, axis=1)

# ML detection
df = apply_ml_detection(df)

# Print anomalies
for _, row in df.iterrows():
    if row["rule_anomalies"] or row["ml_result"] == "ML Anomaly":
        print(f"\n🛰️ Satellite: {row['satellite_id']}")
        print("⚠️ Anomaly Detected")
        print(f"Temperature: {row['temperature']}")
        print(f"Voltage: {row['voltage']}")
        print(f"Current: {row['current']}")
        print(f"Orientation: {row['orientation']}")
        print(f"ML Result: {row['ml_result']}")

# Save report
df.to_csv("../reports/telemetry_analysis_report.csv", index=False)

print("\n✅ Analysis Complete. Report saved.")