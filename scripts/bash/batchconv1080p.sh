#!/bin/bash

for i in *.MP4;
    do name=`echo $i | cut -d'.' -f1`;
    echo $name;
    ffmpeg -i "$i" -r 24 -vf scale=1920:1080,setdar=16:9 1080p/"${name}.MP4";
done
