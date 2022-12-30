abs() {
    if ((0 <= $1)); then
        echo "$1"
    else
        echo "${1:1}"
    fi
}

read -r A B C

if ((C % 2 == 0)); then
    if (($(abs "$A") < $(abs "$B"))); then
        echo '<'
    elif (($(abs "$A") > $(abs "$B"))); then
        echo '>'
    else
        echo '='
    fi
else
    if ((A < B)); then
        echo '<'
    elif ((A > B)); then
        echo '>'
    else
        echo '='
    fi
fi
