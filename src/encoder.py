import pandas
from beeper import Beeper

morse_table = pandas.read_csv("src/data/morse.csv")

beep = Beeper()

# Some redundancy in the encoding. I'm iterating through all the chars in both
# text_to_morse_encoder() and in the beep.beep() method, but I can't be bothered
# to fix it.
def encode(text: str, to_audio: bool):
    morse = text_to_morse_encoder(text)
    if to_audio:
        morse_to_audio(morse)
    return morse

def text_to_morse_encoder(text):
    morse = ""
    for letter in text:
        p_entry = morse_table[morse_table['symbol'] == letter.upper()]['code']
        morse += p_entry.item() if p_entry.size > 0 else "" + " "
    return morse

def morse_to_audio(morse):
    beep.beep(morse)
