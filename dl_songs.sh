
song_url=curl -s $1 | grep -i href  | sed -e 's/^\s*//' -e '/^$/d' | grep 320 | cut -d" -f4

wget $song_url
