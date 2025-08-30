# Sound Event Detection

This project focuses on sound-based event detection and localization, particularly for detecting and localizing whistle sounds. The system employs signal processing methods to achieve accurate detection and localization, with potential applications in surveillance, robotics, and threat detection and prevention.

### Microphone Array
A microphone array consisting of multiple microphones positioned in a circular or linear configuration to capture audio signals from different directions.

### Audio Signal Preprocessing
- Frequency selective filtering to localize whistle in captured signals from microphones.
- Removing echoes from the signals of each microphone.
- Runs an FFT (Fast Fourier Transform) to convert time-domain audio into the frequency domain.
- Extracts magnitudes within the whistle frequency range (WHISTLE_FREQ_RANGE).
- If the magnitude exceeds WHISTLE_THRESHOLD, it flags a whistle event and returns the timestamp.
- This was then used to find cross-correlation between signals from different mics to measure arrival-time differences.

### Stuff Used
- A Raspberry Pi single-board computer serves as the main processing unit.
- Utilized libraries like Python's `PyAudio` for audio processing, `Matplotlib` and `Numpy` for data visualization graphs. 
- Optimized algorithms and computations for the Raspberry Pi's resource constraints.


