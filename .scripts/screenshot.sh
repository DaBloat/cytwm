#!/bin/bash

SCREEN_SHOT=$HOME/Pictures/screenshots/$(date +'%s.png')

grim -g "$(slurp -w 0)" $SCREEN_SHOT
wl-copy --type image/png < "$SCREEN_SHOT"
