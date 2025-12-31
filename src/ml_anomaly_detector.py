from sklearn.ensemble import IsolationForest

def apply_ml_detection(df):
    features = df[["temperature", "voltage", "current", "orientation"]]

    model = IsolationForest(contamination=0.2, random_state=42)
    df["ml_prediction"] = model.fit_predict(features)

    df["ml_result"] = df["ml_prediction"].apply(
        lambda x: "ML Anomaly" if x == -1 else "Normal"
    )

    return df