#!/usr/bin/env bash

wallpaper=$(ls ~/pix/wallpapers/ | shuf -n 1)
path="/home/ghost/pix/wallpapers/"

wal -i $path$wallpaper




