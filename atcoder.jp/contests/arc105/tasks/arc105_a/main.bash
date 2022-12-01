ABCD=$(tr " " "\n" | sort -n)

array=($ABCD)
A=${array[0]}
B=${array[1]}
C=${array[2]}
D=${array[3]}

ans=$((A + B + C == D || A + D == B + C))
((ans)) && echo "Yes" || echo "No"
