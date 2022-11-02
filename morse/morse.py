# -*- coding: utf-8 -*-

"""morse.morse: provides entry point main()."""

__version__ = "0.1.0"

import sys
import time
from pysinewave import SineWave

code = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}

def beep(seconds):
    sinewave = SineWave(pitch=9) # 440 Hz / A
    sinewave.play()
    time.sleep(seconds)
    sinewave.stop()

def toMorse(word):
    converted = ""
    for letter in word:
        morseLetter = code[letter]
        converted = converted + morseLetter + " "
        for char in morseLetter:
            if(char=="-"):
                beep(0.5)
            else:
                beep(0.25)
        time.sleep(0.5)
    return converted

def main():
    for word in sys.argv[1:]:
        print(toMorse(word), end="  ")
        time.sleep(1)