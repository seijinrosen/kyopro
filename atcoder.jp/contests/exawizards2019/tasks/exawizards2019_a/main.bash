read -r A B C

if [ "$A" == "$B" ] && [ "$B" == "$C" ]; then
    echo Yes
else
    echo No
fi
