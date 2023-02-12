#!/usr/bin/env bash
option=$(echo -e "mpc next\nmpc prev\nmpc pause\nmpc toggle\nmpc stop" | rofi -dmenu -i -p "select")
$option -q
notify-send -t 2000 "$option"
