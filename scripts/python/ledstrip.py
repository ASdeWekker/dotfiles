#!/bin/python

# Some imports.
import argparse
import requests


# Some variables.
ip = "http://192.168.1.220/"

# Argparse configuration.
parser = argparse.ArgumentParser(description="Control this ledstrip.")
# Parser arguments, should be explained by the help text.
parser.add_argument("-p", "--power", help="To turn on or off.")
parser.add_argument("-c", "--color", help="Choose a color.")
parser.add_argument("-R", "--rgb", help="Choose a color via rgb value.")
parser.add_argument("-b", "--brightness", help="Choose the brightness.")
parser.add_argument("-H", "--hsv", help="Choose a color via hsv value.")
parser.add_argument("-r", "--rainbow", help="Pick the rainbow function and choose a speed at which the color changes.")
parser.add_argument("-f", "--fade", help="Let the current color fade in and out at the desired speed.")
parser.add_argument("-w", "--wakeup", help="Turn on the wakeup function.", action="store_true")
args = parser.parse_args()

# Check if the power argument was passed and turn it on or off.
if args.power:
	response = requests.post(ip + "power", data={"power": str(args.power)})
	print(response.text)

# Check if the color argument was passed and change the color.
if args.color:
	response = requests.post(ip + "color", data={"color": str(args.color)})
	print(response.text)

# Check if the rgb argument was passed and change the color based on an rgb color value.
if args.rgb:
	response = requests.post(ip + "rgb", data={"rgb": str(args.rgb)})
	print(response.text)

# Check if the hsv argument was passed and .
if args.hsv:
	response = requests.post(ip + "hsv", data={"hsv": str(args.hsv)})
	print(response.text)

# Check if the brightness argument was passed and change the brightness.
if args.brightness:
	response = requests.post(ip + "brightness", data={"brightness": str(args.brightness)})
	print(response.text)

# Check if the rainbow argument was passed and turn on the rainbow with the specified delay.
if args.rainbow:
	response = requests.post(ip + "rainbow", data={"speed": str(args.rainbow)})
	print(response.text)

# Check if the fade argument was passed and fade the color with the specified delay.
if args.fade:
	response = requests.post(ip + "fade", data={"delay": str(args.fade)})
	print(response.text)

# Check if the wakeup argument was passed and start the wake up function.
if args.wakeup:
	response = requests.post(ip + "wakeup")
	print(response.text)
