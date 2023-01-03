max() {
    echo $(($1 < $2 ? $2 : $1))
}

read -r A B
max "$A" "$B"
