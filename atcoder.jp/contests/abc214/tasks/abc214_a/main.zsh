read -r N

if ((N <= 125)); then
    echo 4
elif ((N <= 211)); then
    echo 6
else
    echo 8
fi
