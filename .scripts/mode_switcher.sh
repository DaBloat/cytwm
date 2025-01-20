# This script is for switching to light or dark mode to Hyprland

WALL_PATH=$HOME/wallpaper
LCOLOR_BORDER=331e12
DCOLOR_BORDER=d4baa4
HYPR_CONF=$HOME/.config/hypr/config/aesthetics/looks.conf

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

if [[ $TYPE == 'wall-dark.png' ]] then
	swww img $WALL_PATH/wall.png
	add_to_default $LCOLOR_BORDER 4

elif [[ $TYPE == 'wall.png' ]] then
	swww img $WALL_PATH/wall-dark.png
	add_to_default $DCOLOR_BORDER 0
fi

