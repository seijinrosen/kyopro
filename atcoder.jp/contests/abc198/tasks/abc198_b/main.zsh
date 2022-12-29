is_palindrome() {
    (($1)) && echo $(($(echo "$1" | rev) == $1)) || echo 1
}
rstrip() {
    local s=$1
    local c=$2
    local n=${#s}
    for ((i = n - 1; i >= 0; i--)); do
        if ((${s:$i:1} != c)); then
            break
        fi
        ((n--))
    done
    echo "${s:0:$n}"
}
yes_no() {
    (($1)) && echo "Yes" || echo "No"
}

read -r N
yes_no "$(is_palindrome "$(rstrip "$N" 0)")"
