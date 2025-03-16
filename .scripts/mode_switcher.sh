#!/bin/bash
# This script is for switching to light or dark mode to Hyprland, Kitty

WALL_PATH=$HOME/wallpaper
DCOLOR_BORDER=331e12
LCOLOR_BORDER=d4baa4
HYPR_CONF=$HOME/.config/hypr/config/aesthetics/looks.conf
CYNA_TERMINAL=$HOME/.config/cyna-colors/terminal
CYNA_FABRIC=$HOME/.config/cyna-colors/fabric
KITTY_CCONF=$HOME/.config/kitty/theme.conf
FABRIC_CONF=$HOME/.config/fabric/style/cyna-colors.css

TYPE=$(swww query | awk -F '/' '{print $5}')


# Hyprctl always defaults the color in the conf file every configuration in reload/reboot
# Thus saving it to the looks.conf solve the problem
add_to_default() {
	local color="${1}"
	local ACTIVE="    col.active_border = rgb(${color})"
	local INACTIVE="    col.inactive_border = rgb(${color})"
	local SHADOW_COLOR="        color = rgb(${color})"
	local SHADOW_OFFSET="        offset = $2 $2"



	# Active Border
	if grep -q "col.active_border" "$HYPR_CONF"; then
		sed -i "s/^.*col.active_border.*/$ACTIVE/" "$HYPR_CONF"
	else
		awk '/general {/ { print; print "'"$ACTIVE"'"; next }1' "$HYPR_CONF" > "$HYPR_CONF.tmp" && mv "$HYPR_CONF.tmp" "$HYPR_CONF"
	fi
	
	# Inactive Border
	if grep -q "col.inactive_border" "$HYPR_CONF"; then
		sed -i "s/^.*col.inactive_border.*/$INACTIVE/" "$HYPR_CONF"
	else
		awk '/general {/ { print; print "'"$INACTIVE"'"; next }1' "$HYPR_CONF" > "$HYPR_CONF.tmp" && mv "$HYPR_CONF.tmp" "$HYPR_CONF"
	fi

	# Shadow Color
	if grep -q "color" "$HYPR_CONF"; then
		sed -i "s/^.*color.*/$SHADOW_COLOR/" "$HYPR_CONF"
	else
		awk '/shadow {/ { print; print "'"$SHADOW_COLOR"'"; next }1' "$HYPR_CONF" > "$HYPR_CONF.tmp" && mv "$HYPR_CONF.tmp" "$HYPR_CONF"
	fi

	# Offset
	if grep -q "offset" "$HYPR_CONF"; then
		sed -i "s/^.*offset.*/$SHADOW_OFFSET/" "$HYPR_CONF"
	else
		awk '/shadow {/ { print; print "'"$SHADOW_OFFSET"'"; next }1' "$HYPR_CONF" > "$HYPR_CONF.tmp" && mv "$HYPR_CONF.tmp" "$HYPR_CONF"
	fi
}

change_kitty(){
	local theme=$1
	cat $CYNA_TERMINAL/${1}_colors.conf > $KITTY_CCONF
	$(kill -SIGUSR1 $(pidof kitty)) # Resets kitty to change color
}

change_fabric(){
	local theme=$1
	cat $CYNA_FABRIC/${1}.css > $FABRIC_CONF
}

if [[ $TYPE == 'wall-dark.png' ]] then
	swww img --transition-type wipe --transition-angle 30 --transition-step 60 --transition-fps 120 $WALL_PATH/wall.png
	add_to_default $DCOLOR_BORDER 4
	change_kitty light
	change_fabric creme

elif [[ $TYPE == 'wall.png' ]] then
	swww img --transition-type wipe --transition-angle 210 --transition-step 60 --transition-fps 120 $WALL_PATH/wall-dark.png
	add_to_default $LCOLOR_BORDER 0
	change_kitty dark
	change_fabric coffee
fi