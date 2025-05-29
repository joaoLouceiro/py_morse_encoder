import numpy as np
import pyaudio

DOT_DURATION = 0.05
DASH_DURATION = DOT_DURATION * 3
SPACE_DURATION = DOT_DURATION * 6

class Beeper:

    _instance = None

    def __init__(self) -> None:
        self.p = pyaudio.PyAudio()
        self.sample_rate = 44100  # sampling rate, Hz, must be integer
        self.frequency = 880.0  # sine frequency, Hz, may be float
        self.stream = self.p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=self.sample_rate,
                        output=True)
        print("=== PyAudio initialized ===\n\n")

    def __play(self, volume: float, duration: float):
        samples = (np.sin(2 * np.pi * np.arange(self.sample_rate * duration) * self.frequency / self.sample_rate)).astype(np.float32)
        output_bytes = (volume * samples).tobytes()
        self.stream.write(output_bytes)

    def dot(self):
        self.__play(0.5, DOT_DURATION)
        self.__play(0, DOT_DURATION)

    def dash(self):
        self.__play(0.5, DASH_DURATION)
        self.__play(0, DOT_DURATION)

    def space(self):
        self.__play(0, DASH_DURATION)
        self.__play(0, DOT_DURATION)

    def close_stream(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()


