import pyaudio
import numpy as np
from config import CHUNK, FORMAT, RATE, MIC_DEVICE_IDS

def capture_audio():
    p = pyaudio.PyAudio()
    streams = []
    for device_id in MIC_DEVICE_IDS:
        stream = p.open(format=FORMAT, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK, input_device_index=device_id)
        streams.append(stream)
    return p, streams

def read_stream(stream):
    data = stream.read(CHUNK, exception_on_overflow=False)
    return np.frombuffer(data, dtype=np.int16) / (2 ** 15)
