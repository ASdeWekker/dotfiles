#!/bin/bash

# Location where the files are located
filesloc="/home/alex/dotfiles/conf/5-tmux"
# Location where the files are needed
linkloc="/home/alex/.config/tmuxinator/"

mkdir -p /home/alex/.config/tmuxinator

# For loop to grab all the .yml files and link them
for i in *.yml;
    do echo $i;
    ln -sf $filesloc/$i $linkloc;
done
