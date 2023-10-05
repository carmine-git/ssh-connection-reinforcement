#!/usr/bin/env python

import subprocess

console_output = subprocess.check_output("whoami").decode()
letters = []

for letter in console_output.strip():
    if letter == "\n" or letter == " " or letter == "":
        break
    letters.append(letter)

user = "".join(letters)
