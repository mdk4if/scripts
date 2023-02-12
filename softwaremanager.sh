#!/bin/bash

option=$(echo -e "Install\nRemove\nClean\nUpdate"| rofi -dmenu)

case "$option" in
    "Install") package=$(pacman -Si | awk '/^Name/{name=$3} /^Installed/{is=$4$5} /^Repo/{repo=$3} /^Description/{sub(/^.{18}/,"",$0);print name " ===> ","["is"]","===> " $0} '| rofi -config ~/.scripts/config.rasi -dmenu -i -p "search "| awk '{print $1}')
        sudo pacman -S --noconfirm $package
        notify-send "Installed "
        ;;
    "Remove") remove=$(pacman -Qi | awk '/^Name/{name=$3} /^Download/{is=$4$5} /^Repo/{repo=$3} /^Description/{sub(/^.{18}/,"",$0);print name " ===> ","["is"]", " ===> " $0} '| rofi -config ~/.scripts/config.rasi -dmenu -i -p "search "| awk '{print $1}')
        sudo pacman -Rns --noconfirm $remove
        notify-send "Removed "
        ;;
    "Clean") sudo pacman -Rs $(pacman -Qqtd)
        notify-send "Cleaned UP"
        ;;
    "Update") sudo pacman -Syu --noconfirm
        notify-send "System Updated "
        ;;
    *) notify-send "NO option selected "
        ;;
esac

