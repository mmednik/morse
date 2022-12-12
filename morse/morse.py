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
        letter = str.lower(letter)
        if letter in code: 
            morseLetter = code[letter]
            converted = converted + morseLetter + " "
            for char in morseLetter:
                print(char, end="", flush=True)
                if(char=="-"):
                    beep(0.5/velocity)
                else:
                    beep(0.25/velocity)
            time.sleep(0.5/velocity)
            print(" ", end="", flush=True)

def main():
    global velocity
    velocity = 1
    words = []

    for param in sys.argv[1:]:
        if(param=="--1x"):
            velocity = 1
        elif(param=="--2x"):
            velocity = 2
        elif(param=="--3x"):
            velocity = 3
        else:
            words.append(param)
        

    for word in words:
        toMorse(word)
        time.sleep(1/velocity)