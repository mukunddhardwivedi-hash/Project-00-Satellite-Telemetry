import streamlit as st
import pandas as pd

st.set_page_config(page_title="Satellite Telemetry Dashboard", layout="wide")

st.title("🛰️ Satellite Telemetry Monitoring Dashboard")

df = pd.read_csv("../reports/telemetry_analysis_report.csv")

satellite = st.selectbox("Select Satellite", df["satellite_id"].unique())
filtered = df[df["satellite_id"] == satellite]

st.subheader("Telemetry Parameters")
st.line_chart(filtered[["temperature", "voltage", "current"]])

st.subheader("Anomaly Status")
st.dataframe(filtered[[
    "temperature",
    "voltage",
    "current",
    "orientation",
    "rule_anomalies",
    "ml_result"
]])