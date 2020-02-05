#!/bin/bash

xhost +SI:localuser:wijn
sudo -u wijn env HOME=/home/wijn USER=wijn USERNAME=wijn LOGNAME=wijn wine "$@"