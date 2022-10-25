# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('morse/morse.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "cmdline-morse",
    packages = ["morse"],
    entry_points = {
        "console_scripts": ['morse = morse.morse:main']
        },
    version = version,
    description = "Morse code translator (python command line application)",
    long_description = long_descr,
    author = "Martín Alejandro Mednik",
    author_email = "mmednik@gmail.com",
    url = "https://github.com/mmednik/morse",
    )
