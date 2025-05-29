import pandas

from beeper import Beeper

morse_table = pandas.read_csv("./data/morse.csv")

print(morse_table[morse_table['symbol'] == '!']['code'])

b = Beeper()
m = {'.': b.dot,
     '-': b.dash,
     ' ': b.space}

def text_to_morse_encoder():
    text = input("Tell me: \n").upper()
    morse = ""
    for letter in text:
        p_entry = morse_table[morse_table['symbol'] == letter]['code']
        morse += p_entry.item() if p_entry.size > 0 else "" + " "
    print(morse)
    for c in morse:
        m.get(c, b.space)()

while True:
    text_to_morse_encoder()
