#!/bin/python

# Some imports.
import argparse
import requests


# A small array of power arguments you can pass.
power_args = ["on", "off", "toggle"]

# Argparse config and adding arguments.
parser = argparse.ArgumentParser(description="Turn a switch on or off.")
parser.add_argument("-A", "--all", help="All of them")
parser.add_argument("-o", "--overhead", help="Overhead lamp")
parser.add_argument("-s", "--standing", help="Standing lamp")
parser.add_argument("-a", "--amp", help="Amplifier")
parser.add_argument("-l", "--lights", help="Both lights")
args = parser.parse_args()

# A function to enter the ip address and get the status.
def get(val):
	return "http://192.168.1." + val + "/status"


# A function to enter the ip address and post to the power endpoint.
def post(val):
	return "http://192.168.1." + val + "/power"


# Use this function to check the status of a device.
if args.overhead == "status" or args.standing == "status" or args.amp == "status":
	if args.overhead:
		response = requests.get(get("221"))
		print(response.text)
	if args.standing:
		response = requests.get(get("222"))
		print(response.text)
	if args.amp:
		response = requests.get(get("223"))
		print(response.text)
elif args.all in power_args or args.overhead in power_args or args.standing in power_args or args.amp in power_args:
	if args.all:
		response = requests.post(post("221"), data={"power": str(args.all)})
		print(response.text)
		response = requests.post(post("222"), data={"power": str(args.all)})
		print(response.text)
		response = requests.post(post("223"), data={"power": str(args.all)})
		print(response.text)
	else:
		if args.overhead:
			response = requests.post(post("221"), data={"power": str(args.overhead)})
			print(response.text)
		if args.standing:
			response = requests.post(post("222"), data={"power": str(args.standing)})
			print(response.text)
		if args.amp:
			response = requests.post(post("223"), data={"power": str(args.amp)})
			print(response.text)
		if args.lights:
			response = requests.post(post("221"), data={"power": str(args.lights)})
			print(response.text)
			response = requests.post(post("222"), data={"power": str(args.lights)})
			print(response.text)

