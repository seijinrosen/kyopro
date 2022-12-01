ABCD=$(tr " " "\n" | sort -n | tr "\n" " ")
read A B C D <<<$ABCD

ans=$((A + B + C == D || A + D == B + C))
((ans)) && echo "Yes" || echo "No"
