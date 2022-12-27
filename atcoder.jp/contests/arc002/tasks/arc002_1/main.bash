is_leap() {
    local year=$1
    if ((year % 400 == 0)); then
        echo 1
    elif ((year % 100 == 0)); then
        echo 0
    else
        echo $((year % 4 == 0))
    fi
}
yes_no() {
    (($1)) && echo "YES" || echo "NO"
}

read -r Y
yes_no "$(is_leap "$Y")"
