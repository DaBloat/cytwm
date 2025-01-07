#!/bin/bash


type=$(swww query | awk -F '.' '{print $3}')

exec_path="$( dirname "$(realpath "$0")" )"
path=$(echo "$exec_path" | cut -d '/' -f 1,2,3,4)

if [[ "$type" == "gif" ]]; then
	echo 'Using the Live version, Switching to Static'
	swww img "$path"/wallpapers/okarun/okarun.jpg
else
	echo 'Using the Static version, Switching to Live'
	swww img "$path"/wallpapers/okarun/okarun_live.gif
fi

