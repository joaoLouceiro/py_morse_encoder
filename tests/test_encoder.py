import pytest
import sys
import os

# Add src directory to Python path so we can import module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/')))

from encoder import text_to_morse_encoder

@pytest.mark.parametrize("test_input,expected", [
                            ("", ""),
                            (" ", " "),
                            ("sos", "...---..."),
                            ("sos sos", "...---... ...---...")
                            ]
                         )
def test_a(test_input, expected):
    assert text_to_morse_encoder(test_input) == expected
    

# @patch('encoder.pandas.read_csv')
# def test_text_to_morse_code(read_csv):   
#     read_csv.return_value = pd.read_csv("../src/py_morse_encoder/data/morse.csv")
#     result = text_to_morse_encoder("sos")
#     assert result == "...---..."
    

# @pytest.mark.parametrize("test_input,expected", [("", ""), ("sos", "...---...")])
