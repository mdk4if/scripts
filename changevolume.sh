#!/bin/bash

volume=$(pamixer --get-volume)


case $1 in
up)
	# Set the volume on (if it was muted)
	pamixer -u
	pamixer -i 5 --allow-boost
	
	;;
down)
	pamixer -u
	pamixer -d 5 --allow-boost
	
	;;
mute)
	pamixer -t
	if $(pamixer --get-mute); then
		dunstify -i volume-mute -a "changevolume" -t 2000 -r 9993 -u low "Muted"
	else
		dunstify -a "changevolume" -u low -r "9993" -h int:value:"$volume" -i "volume-$1" "Volume: ${volume}%" -t 2000
	fi
	;;
esac

dunstify -a "changevolume" -u low -r "9993" -h int:value:"$volume" -i "volume-$1" "Volume: ${volume}%" -t 2000
