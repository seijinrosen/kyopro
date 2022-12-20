max() {
    echo $(($1 < $2 ? $2 : $1))
}
min() {
    echo $(($1 < $2 ? $1 : $2))
}

read -r A B C D
(($(max "$A" "$C") <= $(min "$B" "$D"))) && echo "Yes" || echo "No"
