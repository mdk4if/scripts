read -p "[+] Enter path : " path

touch img.txt
touch final.txt

find $path ! -empty -type f -exec md5sum {} + | sort | uniq -w32 -dD img.txt
awk 'NR%2' img.txt > final.txt

while read line; do
  echo "$line"
  rm $line
done <final.txt

rm img.txt
rm final.txt
