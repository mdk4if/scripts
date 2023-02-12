option=$(printf "study\nbookmark" | rofi -dmenu)
case "$option" in
    "study") scrot 'ss_%Y-%m-%d-%s_screenshot.jpg' -e 'mv $f ~/pix/study'
    ;;
    "bookmark") scrot 'ss_%Y-%m-%d-%s_screenshot.jpg' -e 'mv $f ~/pix/bookmark'
    ;;
    *) exit 0
    ;;
esac
#scrot 'ss_%Y-%m-%d-%s_screenshot.jpg' -e 'mv $f ~/pix'

dunstify -a "scrot" -u low -r 9991 "screenshot taken " -t 2000


