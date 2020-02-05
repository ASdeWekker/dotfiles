#!/usr/bin/env bash

sudo virsh attach-device win10 /home/alex/dotfiles/conf/4-vfio/vfioinput/input_mouse.xml --current
sudo virsh attach-device win10 /home/alex/dotfiles/conf/4-vfio/vfioinput/input_keyboard.xml --current
