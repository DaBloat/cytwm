#!/bin/bash

SCREEN_SHOT=$HOME/Pictures/screenshots/$(date +'%s.png')

POS=$(hyprctl activewindow | grep "at:" | awk -F ': ' '{print $2}')
SIZE=$(hyprctl activewindow | grep "size:" | awk -F ': ' '{print $2}' | awk -F ',' '{print $1 "x" $2}')

echo "$(slurp -w 0)"
echo "$POS $SIZE"
grim -g "$POS $SIZE" $SCREEN_SHOT
wl-copy --type image/png < "$SCREEN_SHOT"
