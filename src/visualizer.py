import matplotlib.pyplot as plt

def plot_telemetry(df):

    time = df["time"]

    # TEMPERATURE GRAPH
    plt.figure()
    plt.plot(time, df["temp_c"], marker='o')
    plt.title("Satellite Temperature")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

    # VOLTAGE GRAPH
    plt.figure()
    plt.plot(time, df["voltage_v"], marker='o')
    plt.title("Satellite Voltage")
    plt.xlabel("Time")
    plt.ylabel("Voltage (V)")
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

    # CURRENT GRAPH
    plt.figure()
    plt.plot(time, df["current_a"], marker='o')
    plt.title("Satellite Current")
    plt.xlabel("Time")
    plt.ylabel("Current (A)")
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()
