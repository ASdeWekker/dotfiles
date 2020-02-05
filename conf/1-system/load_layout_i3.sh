#!/bin/bash

# First we append the saved layout of workspace 3 to workspace 3
i3-msg "workspace 3 Dev; append_layout ~/shn/ws3-dev.json"

# Load the needed programs
(subl3 /var/www/html/de_kelder &)
(chromium --new-window http://localhost:3099 &)
(urxvt &)
