# Sound Event Detection and Localization

This project focuses on sound-based event detection and localization, particularly for detecting and localizing whistle sounds. The system employs signal processing methods to achieve accurate detection and localization, with potential applications in surveillance, robotics, and threat detection and prevention.

### Microphone Array
A microphone array consisting of multiple microphones positioned in a circular or linear configuration to capture audio signals from different directions.

### Audio Signal Preprocessing
- Frequency selective filtering to localize whistle in captured signals from microphones.
- Removing echoes from the signals of each microphone.

### Direction Estimation
- Time delay estimation (TDE) techniques to estimate the arrival time differences of the whistle signal at different microphones.
- Triangulation algorithms to estimate the direction of arrival (DOA) based on the TDEs.

### Raspberry Pi
- A Raspberry Pi single-board computer serves as the main processing unit.
- Utilized libraries like Python's `PyAudio` for audio processing, `Matplotlib` and `Numpy` for data visualization graphs. 
- Optimized algorithms and computations for the Raspberry Pi's resource constraints.


