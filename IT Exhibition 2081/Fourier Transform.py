# Import the required libraries

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.signal import sawtooth

t = np.linspace(-30, 30, 1000) # The time for the graph

# Calculating the amplitude which will then make the signal

# Rectangular wave(gives ~sinc function FFT)
signal = np.where(np.abs(t) <= 0.5, 1, 0)

# Step function with sinc FFT(not very continuous)
# signal = np.heaviside(t, 1)

# Triangle pulse
# signal = np.maximum(0, 1 - np.abs(t))

# Gaussian curve with a gaussian curve as an FFT
# signal = np.exp(-t**2 / (2 * (0.1)**2))

# Any random signal
# signal = np.exp(-np.pi * t**2)

# This part of the code is to generate the corresponding frequency values of the FFT.

fft_signal = fft(signal) # Using scipy's fft function
freq = np.fft.fftfreq(len(signal), 1/1000) # The length of the signal, and spacing between sampling points.
                                           # Here since it is 1/1000 it basically means 1000Hz sampling rate.

# This part of the code is the center the FFT at 0.

fft_signal_shifted = np.fft.fftshift(fft_signal)
freq_shifted = np.fft.fftshift(freq)

# Creates the figure of size 12x6.
plt.figure(figsize=(12, 6))

# Plotting the original signal
plt.subplot(2, 1, 1) # Divides the figure into a 2 row, 1 column space and selects the first plot.
plt.plot(t, signal) # Plot the original time and signal(amplitude) graph.
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Original Signal")

# Plotting the transformed signal
plt.subplot(2, 1, 2) # Selects the second plot.
plt.plot(freq_shifted, np.abs(fft_signal_shifted)) # Plot the transformed frequency and magnitude graph.
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.title("Transformed Signal")

# This makes it so that the two plots do not overlap.

plt.tight_layout()

# This shows the plot.

plt.show()
