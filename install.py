#!/usr/bin/env python

import subprocess

user_console_output = subprocess.call("whoami", shell=True)
print(user_console_output)
