from numpy.typing import NDArray
import pandas
import numpy as np
import matplotlib.pyplot as plt

from pydub import AudioSegment
from signal_tuple import SignalTuple

morse_table = pandas.read_csv("src/data/morse.csv")


class Decoder:
    def __init__(self, file_path: str) -> None:
        file_format = file_path.split("/")[-1].split(".")[-1]
        self.__audio_segment = AudioSegment.from_file(file_path, format=file_format)

    def decode(self):
        sample_array = self.__parse_audio_segment_to_nparray()
        smooth_df = self.__smooth_out_and_clean_data(sample_array)
        signal_and_silence_pair_array = self.__make_signal_silence_pair_array(smooth_df)
        morse_code = self.__convert_signal_array_to_morse_code(signal_and_silence_pair_array)
        print(self.__convert_morse_symbols_to_text(morse_code))

    def __parse_audio_segment_to_nparray(self):
        sample_array = np.array(self.__audio_segment.get_array_of_samples())
        return sample_array.reshape((-1, 1))

    def __smooth_out_and_clean_data(self, sample_array: NDArray) -> pandas.DataFrame | pandas.Series:
        df = pandas.DataFrame(np.absolute(sample_array))
        rolling_df = df.rolling(window=1000).mean()
        clean_df = rolling_df.dropna()
        return clean_df


    def __make_signal_silence_pair_array(self, df: pandas.DataFrame | pandas.Series):
        avg_signal_intensity = df.mean().item()

        is_signal = False
        s_start = 0
        s_end = 0
        signal_length = 0
        silence_length = 0

        signal_tuple = SignalTuple()
        signal_array = []

        for index, frame in enumerate(df[0]):
            if not is_signal and frame > avg_signal_intensity:
                is_signal = True
                s_start = index

                silence_length = s_start - s_end

                if signal_tuple.__signal_length__ > 0:
                    signal_tuple.set_silence_length(silence_length)
                    signal_array.append(signal_tuple.get_tuple())
                    signal_tuple = SignalTuple()

            elif is_signal and frame < avg_signal_intensity:
                is_signal = False
                s_end = index
                signal_length = s_end - s_start

                signal_tuple.set_signal_length(signal_length)

        if signal_tuple.__signal_length__ is not None:
            signal_array.append(signal_tuple.get_tuple())

        return np.array(signal_array)

    def __convert_signal_array_to_morse_code(self, signal_array) -> str:
        avg_signal_length = signal_array.mean(axis=0)[0]
        out = ""
        for signal, silence in signal_array:
            if signal < avg_signal_length:
                out += "."
            else:
                out += "-"

            if silence > avg_signal_length* 3:
                out += "   "
            elif silence > avg_signal_length:
                out += " "
            else:
                out += ""
        return out

    def __convert_morse_symbols_to_text(self, morse_string: str) -> str:
        split_str = morse_string.split(" ")
        out = ""
        for code in split_str:
            if code == "":
                out += " "
            else:
                try:
                    out += morse_table['symbol'][morse_table["code"] == code].values[0]
                except IndexError:
                    out += "!"
        return out



    def __debug_plot_signal(self, df: pandas.DataFrame):
        fig = plt.figure(figsize=(16,8))
        ax = plt.gca()

        ax.plot(df)
        plt.show()

