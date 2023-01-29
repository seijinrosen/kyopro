abs() {
    if ((0 <= $1)); then
        echo "$1"
    else
        echo "${1:1}"
    fi
}

read -r A B

absA=$(abs "$A")
absB=$(abs "$B")

if ((absA < absB)); then
    echo "Ant"
elif ((absA == absB)); then
    echo "Draw"
else
    echo "Bug"
fi
