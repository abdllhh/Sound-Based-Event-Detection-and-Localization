import unittest
from audio_processing.audio_capture import capture_audio, read_stream

class TestAudioCapture(unittest.TestCase):

    def test_capture_audio(self):
        p, streams = capture_audio()
        self.assertEqual(len(streams), 3)
        p.terminate()

    def test_read_stream(self):
        p, streams = capture_audio()
        data = read_stream(streams[0])
        self.assertEqual(len(data), 1024 * 4)
        p.terminate()

if __name__ == '__main__':
    unittest.main()
