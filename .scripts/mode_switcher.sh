# This script is for switching to light or dark mode to whole system

WALL_PATH=$HOME/wallpaper
LCOLOR_BORDER=331e12
DCOLOR_BORDER=d4baa4 

hyprctl reload

if [[ $1 == 'l' ]] then
	echo 'Light MODE ON'
	swww img $WALL_PATH/wall.png
	hyprctl --batch "keyword general:col.active_border 0xFF${LCOLOR_BORDER} ;
			 keyword general:col.inactive_border 0xFF${LCOLOR_BORDER} ;
			 keyword decoration:shadow:color 0xFF${LCOLOR_BORDER};
			 keyword decoration:shadow:offset 4 4 ;
			 keyword decoration:shadow:scale 1.0"
elif [[ $1 == 'd' ]] then
	echo 'Dark MODE ON'
	$(swww img $WALL_PATH/wall-dark.png)
	hyprctl --batch "keyword general:col.active_border 0xFF${DCOLOR_BORDER} ; keyword general:col.inactive_border 0xFF${DCOLOR_BORDER}"
fi

