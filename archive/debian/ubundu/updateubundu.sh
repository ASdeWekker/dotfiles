#!/bin/bash

echo "Updating Ubuntu..."
sudo apt update;
sudo apt upgrade;
sudo apt full-upgrade;
echo "...";
sudo apt autoclean;
sudo apt autoremove;
