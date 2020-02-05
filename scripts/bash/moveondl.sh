#!/bin/bash

if [ -z "$(ls -A /srv/deluge/Downloads/complete/)" ]; then
    exit
else
    chown -R alex:wheel /srv/deluge/Downloads/complete/*
    mv /srv/deluge/Downloads/complete/* /mnt/data/videos/
fi
