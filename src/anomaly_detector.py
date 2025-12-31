def rule_based_detection(row):
    if row["temperature"] > 80:
        return True
    if row["voltage"] < 3.0 or row["voltage"] > 4.2:
        return True
    if row["current"] > 2.5:
        return True
    if abs(row["orientation"]) > 45:
        return True
    return False