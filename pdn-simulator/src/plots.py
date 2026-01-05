import matplotlib.pyplot as plt

def plot_voltage(time, voltage):
    plt.figure()
    plt.plot(time * 1e6, voltage)
    plt.xlabel("Time (µs)")
    plt.ylabel("Voltage (V)")
    plt.title("PDN Voltage Transient")
    plt.grid()
    plt.show()
