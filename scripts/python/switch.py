#!/bin/python


# Some imports.
import argparse
import requests as req


# A small list of power arguments you can pass.
POWER_ARGS = ["on", "off", "toggle"]
# List for the ip addresses, only the last number though.
IPS = ["1", "2", "3"]

# Argparse config and adding arguments.
parser = argparse.ArgumentParser(description="Turn a switch on or off.")
parser.add_argument("-A", "--all", help="All of them")
parser.add_argument("-o", "--overhead", help="Overhead lamp")
parser.add_argument("-s", "--standing", help="Standing lamp")
parser.add_argument("-a", "--amp", help="Amplifier")
parser.add_argument("-l", "--lights", help="Both lights")
args = parser.parse_args()

# Another list, this one is for the arguments.
ARGS = [args.all, args.overhead, args.standing, args.amp, args.lights]


# A function to enter the ip address and get the status.
def get(val):
	return "http://192.168.1.22%s/status" % (val)


# A function to enter the ip address and post to the power endpoint.
def post(val):
	return "http://192.168.1.22%s/power" % (val)


# Use this function to check the status of a device.
if "status" in ARGS:
	if args.all:
		for i in IPS:
			res = req.get(get(i))
	if args.overhead:
		res = req.get(get("1"))
	if args.standing:
		res = req.get(get("2"))
	if args.amp:
		res = req.get(get("3"))
	if args.lights:
		res = req.get(get("1"))
		res = req.get(get("2"))
# Check if one of the power arguments have been passed so execute those.
elif any(i in POWER_ARGS for i in ARGS):
	# Check if -A has been passed, otherwise check for the individual ones.
	if args.all:
		for i in IPS:
			res = req.post(post(i), data={"power": str(args.all)})
	if args.overhead:
		res = req.post(post("1"), data={"power": str(args.overhead)})
	if args.standing:
		res = req.post(post("2"), data={"power": str(args.standing)})
	if args.amp:
		res = req.post(post("3"), data={"power": str(args.amp)})
	if args.lights:
		res = req.post(post("1"), data={"power": str(args.lights)})
		res = req.post(post("2"), data={"power": str(args.lights)})
print(res.text)
