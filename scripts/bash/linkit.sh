#!/bin/bash

ulb="/usr/local/bin"
dot="/home/alex/dotfiles/scripts/bash"
sudo ln -sf $dot/batchconv1080p.sh $ulb/conv1080
sudo ln -sf $dot/batchconv24fps.sh $ulb/conv24
sudo ln -sf $dot/runaswine.sh $ulb/wijn
sudo ln -sf $dot/create-pug.sh $ulb/create-pug
sudo ln -sf $dot/../python/switch.py $ulb/sw
sudo ln -sf $dot/../python/ledstrip.py $ulb/led
