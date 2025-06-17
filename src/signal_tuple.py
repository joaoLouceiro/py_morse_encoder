"""
A signal will only be measured by contrast with a silence.
By keeping track of the signal and it's following silence, I am 
able to determine if I am in between dots/dashes within a letter,
between letters, or between words.

'And just remember everything you are is more important to realize
 the negative space as music is only the division of space. It is 
 the space we are listening to divided as such which gives us the 
 information in comparison to something other that gives us the idea 
 of what the idea that wants to be transmitted wants to be. 
 So please without further ado.'
 - Reggie Watts, TedX, 2012
"""
class SignalTuple:
    def __init__(self) -> None:
        self.__signal_length__ = 0
        self.__silence_length__ = 0

    def set_signal_length (self, length: int) -> None:
        self.__signal_length__ = length

    def set_silence_length(self, length: int) -> None:
        self.__silence_length__ = length

    def get_tuple(self) -> tuple[int, int]:
        return self.__signal_length__, self.__silence_length__

    def __str__(self) -> str: 
        return f"({self.__signal_length__}, {self.__silence_length__})"