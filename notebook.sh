#!/usr/bin/env bash

path="/home/$USER/.Notebook"
if [[ ! -d $path ]]; then
    notify-send "directory made"
    mkdir -p $path
fi
ops=$(echo -e "ADD\nEDIT\nREAD\nDELETE" | rofi -dmenu -i -p "Notebook")
case "$ops" in
    "ADD") addnote=$(rofi -dmenu -p "Enter file name") && st -e nvim "$path/$addnote.txt"
        ;;
    "EDIT") editnote=$(ls $path | rofi -dmenu -i -p "select") && st -e nvim "$path/$editnote"
        ;;
    "READ") readnote=$(ls $path | rofi -dmenu -i -p "select") && st -e nvim "$path/$readnote"
        ;;
    "DELETE") delnote=$(ls $path | rofi -dmenu -i -p "select") && st -e rm "$path/$delnote"
        ;;
esac
