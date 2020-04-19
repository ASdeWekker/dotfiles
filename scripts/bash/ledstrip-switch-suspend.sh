#!/bin/bash

if [ "${1}" == "pre" ]; then
	/usr/bin/python3 /home/alex/dotfiles/scripts/python/ledstrip.py -p off
elif [ "${1}" == "post" ]; then
	/usr/bin/python3 /home/alex/dotfiles/scripts/python/ledstrip.py -r 222
fi
