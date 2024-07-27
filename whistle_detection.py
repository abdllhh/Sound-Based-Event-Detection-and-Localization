import numpy as np
from datetime import datetime
from config import RATE, CHUNK, WHISTLE_THRESHOLD, WHISTLE_FREQ_RANGE

def detect_whistle(data):
    spectrum = np.fft.fft(data)
    magnitude = np.abs(spectrum[:CHUNK // 2]) * 2 
    whistle_magnitude = magnitude[(np.linspace(0, RATE / 2, CHUNK // 2) >= WHISTLE_FREQ_RANGE[0]) & 
                                  (np.linspace(0, RATE / 2, CHUNK // 2) <= WHISTLE_FREQ_RANGE[1])]
    if np.max(whistle_magnitude) > WHISTLE_THRESHOLD:
        return True, datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return False, None
