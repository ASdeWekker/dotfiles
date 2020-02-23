#!/bin/python


# Some imports.
import argparse
import requests


# A small array of power arguments you can pass.
POWER_ARGS = ["on", "off", "toggle"]

# Argparse config and adding arguments.
parser = argparse.ArgumentParser(description="Turn a switch on or off.")
parser.add_argument("-A", "--all", help="All of them")
parser.add_argument("-o", "--overhead", help="Overhead lamp")
parser.add_argument("-s", "--standing", help="Standing lamp")
parser.add_argument("-a", "--amp", help="Amplifier")
parser.add_argument("-l", "--lights", help="Both lights")
args = parser.parse_args()

# Another array, this one is for the arguments.
ARGS = [args.all, args.overhead, args.standing, args.amp, args.lights]


# A function to enter the ip address and get the status.
def get(val):
	return "http://192.168.1.22%s/status" % (val)


# A function to enter the ip address and post to the power endpoint.
def post(val):
	return "http://192.168.1.22%s/power" % (val)


# Use this function to check the status of a device.
if any ("status" for i in ARGS):
	if args.overhead:
		response = requests.get(get("1"))
	if args.standing:
		response = requests.get(get("2"))
	if args.amp:
		response = requests.get(get("3"))
# Otherwise check if one of the power arguments have been passed so execute those
elif any (i in POWER_ARGS for i in ARGS):
	# Check if -A has been passed, otherwise check for the individual ones.
	if args.all:
		response = requests.post(post("1"), data={"power": str(args.all)})
		response = requests.post(post("2"), data={"power": str(args.all)})
		response = requests.post(post("3"), data={"power": str(args.all)})
	else:
		if args.overhead:
			response = requests.post(post("1"), data={"power": str(args.overhead)})
		if args.standing:
			response = requests.post(post("2"), data={"power": str(args.standing)})
		if args.amp:
			response = requests.post(post("3"), data={"power": str(args.amp)})
		if args.lights:
			response = requests.post(post("1"), data={"power": str(args.lights)})
			response = requests.post(post("2"), data={"power": str(args.lights)})
print(response.text)
