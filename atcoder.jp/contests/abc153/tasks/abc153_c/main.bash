sum() {
    local result=0
    for x in $1; do
        ((result += x))
    done
    echo $result
}

read -r _N K

x=$(tr " " "\n" | sort --numeric-sort --reverse | tail +$((K + 1)))
sum "$x"
