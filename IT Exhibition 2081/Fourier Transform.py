import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.signal import sawtooth

t = np.linspace(-30, 30, 1000)

signal = np.where(np.abs(t) <= 0.5, 1, 0) # rectangular wave(gives ~sinc function fft)
# signal = np.heaviside(t, 1) # step function with sinc fft(not very continuous)
# signal = np.maximum(0, 1 - np.abs(t)) # triangle pulse
# signal = np.exp(-t**2 / (2 * (0.1)**2)) # Gaussian curve with a gaussian curve as fft
# signal = np.exp(-np.pi * t**2) # random signal

fft_signal = fft(signal)
freq = np.fft.fftfreq(len(signal), 1/1000)

fft_signal_shifted = np.fft.fftshift(fft_signal)
freq_shifted = np.fft.fftshift(freq)

# plot
plt.figure(figsize=(12, 6))

# ORIGINAL PLOT
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Original Signal")

# FFT PLOT
plt.subplot(2, 1, 2)
plt.plot(freq_shifted, np.abs(fft_signal_shifted))
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.title("Transformed Signal")

plt.tight_layout()
plt.show()
