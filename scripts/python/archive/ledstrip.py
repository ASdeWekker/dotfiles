#!/bin/python

# Some imports.
import argparse
import requests as req


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
parser.add_argument("-s", "--status", help="Check the status of the ledstrip", action="store_true")
args = parser.parse_args()

# Check if the power argument was passed and turn it on or off.
if args.power:
	res = req.post("%spower" % (ip), data={"power": str(args.power)})
# Check if the color argument was passed and change the color.
if args.color:
	res = req.post("%scolor" % (ip), data={"color": str(args.color)})
# Check if the rgb argument was passed and change the color based the value.
if args.rgb:
	res = req.post("%srgb" % (ip), data={"rgb": str(args.rgb)})
# Check if the hsv argument was passed and .
if args.hsv:
	res = req.post("%shsv" % (ip), data={"hsv": str(args.hsv)})
# Check if the brightness argument was passed and change the brightness.
if args.brightness:
	res = req.post("%sbrightness" % (ip), data={"brightness": str(args.brightness)})
# Check if the rainbow argument was passed and turn on the rainbow with the specified delay.
if args.rainbow:
	res = req.post("%srainbow" % (ip), data={"speed": str(args.rainbow)})
# Check if the fade argument was passed and fade with the specified delay.
if args.fade:
	res = req.post("%sfade" % (ip), data={"delay": str(args.fade)})
# Check if the wakeup argument was passed and start the wake up function.
if args.wakeup:
	res = req.post("%swakeup" % (ip))
# Check the status of the ledstrip.
if args.status:
	res = req.post("%sstatus" % (ip))
print(res.text)
