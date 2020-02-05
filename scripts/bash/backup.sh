#!/bin/bash

# use a command to backup the root directory once per 3 nights
# use a command to backup the home folder every night
# tar and gzip the resulting stuff in the that should be
# outputted to the rsync folder in the Backup folder
# make a structure where it will eventually hold a backup
# of every month.
# figure out how to connect with ssh to the pi - figured it out!

# The backup will go as follows:
# - pi root
# - pi home
# - pc home
# - pc root


# location of the backup folder:
# bloc="/mnt/backup"
# # location were the tar.gz's are stored
# gzloc="/mnt/data/backup/gzip"

# # root pi commands:
# # backup
# rsync -aAXvq -e ssh --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found","/home/*","/var/www/html/backup/*"} taartr:/ $bloc/rsync/pi-root/

# # tar and gzip
# env GZIP=-9 tar czf $gzloc/pi/$(date -I)-pi-root.tar.gz $bloc/rsync/pi-root/*

# # sleep for a bit
# sleep 2

# # home pi commands:
# rsync -aAXvq -e ssh --exclude={"/home/*/.thumbnails/*","/home/*/.cache/mozilla/*","/home/*/.cache/chromium/*","/home/*/.local/share/Trash/*","/home/*/.gvfs","/home/*/shn/*"} taartr:/home/alex/ $bloc/rsync/pi-home/

# # tar and gzip
# env GZIP=-9 tar czf $gzloc/pi/$(date -I)-pi-home.tar.gz $bloc/rsync/pi-home/*

# # sleep for a bit
# sleep 2

# # home pc commands:
# rsync -aAXvq --exclude={"/home/*/.thumbnails/*","/home/*/.cache/mozilla/*","/home/*/.cache/chromium/*","/home/*/.local/share/Trash/*","/home/*/.gvfs","/home/*/shn/*"} /home/alex/ $bloc/rsync/pc-home/

# # tar and gzip
# env GZIP=-9 tar czf $gzloc/pc/$(date -I)-pc-home.tar.gz $bloc/rsync/pc-home/*

# # sleep for a bit
# sleep 2

# # root pc commands:
# rsync -aAXvq --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found","/home/*","/var/www/html/backup/*"} / $bloc/rsync/pc-root/

# # tar and gzip
# env GZIP=-9 tar czf $gzloc/pc/$(date -I)-pc-root.tar.gz $bloc/rsync/pc-root/*

# # sleep for a bit
# sleep 2

# # shutdown system
# systemctl poweroff

