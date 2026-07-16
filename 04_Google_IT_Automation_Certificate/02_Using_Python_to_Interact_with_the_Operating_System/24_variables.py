#!/usr/bin/env python3
import os
print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))

#set FRUIT=Pineapple for terminal to set the output of FRUIT variable
#$env:FRUIT="Pineapple" for powershell to set the output of FRUIT variable
# echo %PATH% for windows command prompt to see the paths