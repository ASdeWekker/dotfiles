#!/bin/python

import argparse
import requests


# Some variables.
ip = "http://192.168.1.220/"

# Argparse configuration.
parser = argparse.ArgumentParser(description="Control this ledstrip.")
parser.add_argument("-p", "--power", help="To turn on or off.")
parser.add_argument("-c", "--color", help="Choose a color.")
parser.add_argument("-R", "--rgb", help="Choose a color via rgb value.")
parser.add_argument("-b", "--brightness", help="Choose the brightness.")
parser.add_argument("-H", "--hsv", help="Choose a color via hsv value.")
parser.add_argument("-r", "--rainbow", help="Pick the rainbow function and choose a speed at which the color changes.")
parser.add_argument("-f", "--fade", help="Let the current color fade in and out at the desired speed.")
parser.add_argument("-w", "--wakeup", help="Turn on the wakeup function.", action="store_true")
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

if args.fade:
	response = requests.post(ip + "fade", data={"delay": str(args.fade)})
	print(response.text)

if args.wakeup:
	response = requests.post(ip + "wakeup")
	print(response.text)
