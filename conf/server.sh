#!/bin/bash

#==========================================================#
### This file is used to link configuration files in the ###
### system after a fresh install on a server.            ###
#==========================================================#

# using some home variables.
home="/home/alex"
homed="/home/alex/dotfiles/conf"

# Display all the commands used.
set -x

### 1 - System ###
# network
sudo cp $homed/1-system/server.network /etc/systemd/network/eno1.network
sudo systemctl reenable systemd-networkd

# NFS
# not going to use nfs for a while
# sudo ln -sf $homed/1-system/server-nfs-exports /etc/exports

# snapRAID
sudo ln -sf $homed/1-system/snapraid.conf /etc/

### 2 - Misc ###
# Samba
sudo ln -sf $homed/2-misc/server-smb.conf /etc/samba/smb.conf
mkdir -p /home/alex/public
mkdir -p /home/alex/downloads
sudo systemctl reenable smb nmb

# EOF 
