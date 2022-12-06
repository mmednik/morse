morse
=====

**morse** is a command line tool that allows you to translate text into Morse code and play the corresponding sound for each letter.

Usage
-----

To use morse, run the following command in the terminal:

```
morse.py [--speed] <text>
```
where **speed** is the desired speed (optional) and text is the text you want to translate into Morse code.

The speed can be specified as **--1x**, **--2x** or **--3x**, where 1x is the standard speed, 2x is twice the speed and 3x is three times the speed.


### Examples:

```
python morse.py hello world
python morse.py --2x hello world
python morse.py --3x hello world
```