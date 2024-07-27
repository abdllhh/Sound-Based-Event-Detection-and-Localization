import matplotlib.pyplot as plt
import numpy as np

def initialize_plot(num_mics):
    fig, axs = plt.subplots(num_mics, 2, figsize=(15, 15))
    return fig, axs

def update_waveform_plot(ax, data, color):
    ax.clear()
    ax.plot(data, color=color)
    ax.set_ylim(-1, 1)
    ax.set_xlim(0, len(data))
    ax.set_title('Audio Waveform')
    ax.set_xlabel('Samples')
    ax.set_ylabel('Amplitude')

def update_spectrum_plot(ax, data, color):
    ax.clear()
    freqs = np.fft.fftfreq(len(data), 1/44100)
    ax.semilogx(freqs[:len(data)//2], np.abs(data)[:len(data)//2], color=color)
    ax.set_xlim(20, 20000)
    ax.set_ylim(0, np.max(np.abs(data)))
    ax.set_title('Audio Spectrum')
    ax.set_xlabel('Frequency [Hz]')
    ax.set_ylabel('Magnitude')
