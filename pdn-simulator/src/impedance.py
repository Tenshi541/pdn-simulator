import numpy as np
# industry standard FFT Impedance method
def compute_impedance(time, voltage, current):
    V_fft = np.fft.fft(voltage)
    I_fft = np.fft.fft(current)

    freq = np.fft.fftfreq(len(time), time[1] - time[0])
    Z = np.abs(V_fft) / np.abs(I_fft)

    return freq[:len(freq)//2], Z[:len(Z)//2]
