sum() {
    local result=0
    for x in $1; do
        ((result += x))
    done
    echo $result
}

read -r A B

array=()

if ((A < B)); then
    for ((i = 1; i <= B; i++)); do
        array+=(-"$i")
    done
    for ((i = 1; i < A; i++)); do
        array+=("$i")
    done
else
    for ((i = 1; i <= A; i++)); do
        array+=("$i")
    done
    for ((i = 1; i < B; i++)); do
        array+=(-"$i")
    done
fi

array+=($((-$(sum "${array[*]}"))))
echo "${array[@]}"
