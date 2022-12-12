morse
=====

**morse** is a command line tool that allows you to translate text into Morse code and play the corresponding sound for each letter.


Installation
------------

Clone this repo and run the following command in the terminal:

:code:`python setup.py install`


Usage
-----

To use morse, run the following command in the terminal:

:code:`morse [--speed] <text>`

where **speed** is the desired speed (optional) and text is the text you want to translate into Morse code.

The speed can be specified as **--1x**, **--2x** or **--3x**, where 1x is the standard speed, 2x is twice the speed and 3x is three times the speed.


Examples
--------

:code:`morse hello world`

:code:`morse --2x hello world`

:code:`morse --3x hello world`