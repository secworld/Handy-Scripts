#! /bin/bash

while IFS='' read -r i; do
    echo "For IP ==> $i"
    printf "\n\n testssl $i\n\n"
    ./testssl $i
    printf "\n\n nc $i 80\n\n"
    nc $i 80 #copy this and paste GET / HTTP/1.1
    printf "\n\n ssh root@$i\n\n"
    ssh root@$i 
    printf "\n\n cisco-torch $i \n\n"
    cisco-torch -A $i
    printf "\n\n nc $i 21 \n\n"
    nc $i 21
    printf "\n\n nc $i 25 \n\n"
    nc $i 25

done < "$1"
