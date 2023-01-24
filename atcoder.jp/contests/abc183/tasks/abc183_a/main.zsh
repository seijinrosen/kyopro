relu() {
    local x=$1

    if ((x >= 0)); then
        echo "$1"
    else
        echo 0
    fi
}

read -r x

ans=$(relu "$x")

echo "$ans"
