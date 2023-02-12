#!/bin/bash

function send_notification() {
	brightness=$(printf "%.0f\n" $(brillo -G))
	dunstify -a "changebrightness" -u low -r 1337 -h int:value:"$brightness"  "$brightness $1" -t 2000
}

case $1 in
up)
	brillo -A 5 -q
	send_notification $1
	;;
down)
	brillo -U 5 -q
	send_notification $1
	;;
esac
