#!/usr/bin/env bash

path="/home/king/pix/wallpapers/"
wall=$(ls /home/$USER/pix/wallpapers/ | shuf -n 1)
betterlockscreen -u $path$wall
