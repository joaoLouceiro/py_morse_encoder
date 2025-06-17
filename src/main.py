import encoder
from decoder import Decoder
from pathlib import Path


while True:
    opt = input("1. Encode\n2. Decode\n3. Exit\n") 
    if opt == "1":
        to_audio = True if input("\n\t1. On screen\n\t2. Screen and Audio\n") else False
        text = input("Type away\n")
        encoder.encode(text, to_audio)
    elif opt == "2":
        file_path = input("Choose file:\n")
        file = Path(file_path)
        if file.is_file():
            decoder = Decoder(file_path=file_path)
            decoder.decode()
        else:
            print(f"{file_path} does not exist or isn't a file")
    elif opt == "3":
        break
    else:
        print("invalid option\n")


print("Goodbye!")

