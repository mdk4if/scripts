#!/bin/bash

editfile=$(find /home/$USER/.config/ -print | rofi -dmenu -i -p "select")
notify-send "Opening $editfile"
nvim $editfile
