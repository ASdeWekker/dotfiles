#!/bin/python

# Some imports.
import argparse
import requests


# Argparse config and adding arguments.
parser = argparse.ArgumentParser(description="Turn a switch on or off.")
parser.add_argument("-A", "--all", help="All of them")
parser.add_argument("-o", "--overhead", help="Overhead lamp")
# parser.add_argument("-s", "--standing", help="Standing lamp")
parser.add_argument("-a", "--amp", help="Amplifier")
args = parser.parse_args()


# A function to enter the ip address.
def ip(val):
	return "http://192.168.1." + val + "/power"


# Check which arg was passed and act accordingly.
if args.all:
	response = requests.post(ip("221"), data={"power": str(args.all)})
	# response = requests.post(ip("222"), data={"power": str(args.all)})
	response = requests.post(ip("223"), data={"power": str(args.all)})
else:
	if args.overhead:
		response = requests.post(ip("221"), data={"power": str(args.overhead)})
	# if args.standing:
	# 	response = requests.post(ip("222"), data={"power": str(args.standing)})
	if args.amp:
		response = requests.post(ip("223"), data={"power": str(args.amp)})

