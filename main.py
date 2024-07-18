import time
import threading
from queue import Queue, Empty

from config import CHUNK, NUM_MICROPHONES
from audio_processing.audio_capture import capture_audio, read_stream
from audio_processing.whistle_detection import detect_whistle
from utils.plotting import initialize_plot, update_waveform_plot, update_spectrum_plot

def main():
    p, streams = capture_audio()
    fig, axs = initialize_plot(NUM_MICROPHONES)

    def process_microphone_data(i):
        stream = streams[i]
        while not stop_flag.is_set():
            data = read_stream(stream)
            whistle, timestamp = detect_whistle(data)
            if whistle:
                print(f"Whistle detected on Microphone {i+1} at: {timestamp}")
                stop_flag.set()
            queue.put((i, data))

    threads = []
    stop_flag = threading.Event()
    queue = Queue(maxsize=20)

    for i in range(NUM_MICROPHONES):
        t = threading.Thread(target=process_microphone_data, args=(i,))
        t.daemon = True
        threads.append(t)
        t.start()

    try:
        while not stop_flag.is_set():
            batch_data = []
            while not queue.empty() and len(batch_data) < NUM_MICROPHONES:
                try:
                    batch_data.append(queue.get_nowait())
                except Empty:
                    pass

            for i, data in batch_data:
                update_waveform_plot(axs[i, 0], data, 'r')
                update_spectrum_plot(axs[i, 1], np.fft.fft(data), 'b')
            if batch_data:
                fig.canvas.draw()
                fig.canvas.flush_events()
            time.sleep(0.01)
    except KeyboardInterrupt:
        pass

    for stream in streams:
        stream.stop_stream()
        stream.close()
    p.terminate()

if __name__ == "__main__":
    main()
  
