#!/bin/python

import subprocess

print("You're going to link some files aren't you?")
print("0 - Desktop")
print("1 - Raspberry Pi")
print("2 - Server")
answer = input("On which system? ")

if answer == "0":
    print("Dekstop")
    subprocess.call(["/home/alex/dotfiles/conf/desktop.sh"])
elif answer == "1":
    print("Raspberry Pi")
    subprocess.call(["/home/alex/dotfiles/conf/rpi.sh"])
elif answer == "2":
    print("Server")
    subprocess.call(["/home/alex/dotfiles/conf/server.sh"])
else:
    print("beter typen pik")
subprocess.call(["/home/alex/dotfiles/conf/main.sh"])