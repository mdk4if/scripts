#!/bin/bash
printf "Enter link : "
read link
printf "Enter album name : "
read albumname
mkdir -p "$albumname"

curl -s "$link" | grep -oiE "https://pagalnew.com/songs/.*" | cut -d\" -f1 | sort | uniq > dl.txt

while read line

do 
	aria2c -q -d "$albumname" "https://pagalnew.com$(curl -s "$line" | grep "320 KBPS Song Download" | cut -d'"' -f8 )"  
	echo "Downloading $line"

done < dl.txt





