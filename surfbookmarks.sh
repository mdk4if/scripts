#!/bin/bash

url=$(cat ~/.scripts/bookmarks.txt | rofi -dmenu -p "bookmarks")
sure=$(printf "Sure bro\nNaah" | rofi -dmenu -p "sure")
case "$sure" in
    "Sure bro") firefox $url
    ;;
    *) notify-send "bye bye"
    ;;
esac
