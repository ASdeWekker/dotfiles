#!/bin/python

import argparse
import requests


# Some variables.
ip = "http://192.168.1.220/"

# Argparse configuration.
parser = argparse.ArgumentParser(description="control this ledstrip.")
parser.add_argument("-p", "--power", help="to turn on or off.")
parser.add_argument("-c", "--color", help="choose a color.")
parser.add_argument("-r", "--rgb", help="choose a color via rgb value.")
parser.add_argument("-b", "--brightness", help="choose the brightness.")
parser.add_argument("-H", "--hsv", help="choose a color via hsv value.")
parser.add_argument("-R", "--rainbow", help="pick the rainbow function and choose a speed at which the color changes.")
args = parser.parse_args()

# Check if the power argument was passed and execute the function.
if args.power:
	response = requests.post(ip + "power", data={"power": str(args.power)})
	print(response.text)

if args.color:
	response = requests.post(ip + "color", data={"color": str(args.color)})
	print(response.text)

if args.rgb:
	response = requests.post(ip + "rgb", data={"rgb": str(args.rgb)})
	print(response.text)

if args.hsv:
	response = requests.post(ip + "hsv", data={"hsv": str(args.hsv)})
	print(response.text)

if args.brightness:
	response = requests.post(ip + "brightness", data={"brightness": str(args.brightness)})
	print(response.text)

if args.rainbow:
	response = requests.post(ip + "rainbow", data={"speed": str(args.rainbow)})
	print(response.text)
