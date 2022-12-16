max() {
    echo $(($1 < $2 ? $2 : $1))
}
min() {
    echo $(($1 < $2 ? $1 : $2))
}

read -r N A B
echo "$(min A B)" "$(max 0 $((A + B - N)))"
