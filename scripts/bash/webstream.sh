#!/bin/bash

sudo mjpg_streamer -i "/usr/local/lib/mjpg-streamer/input_uvc.so"  -o "/usr/local/lib/mjpg-streamer/output_http.so -w /home/alex/www"
