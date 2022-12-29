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
sum() {
    local result=0
    for x in $@; do
        ((result += x))
    done
    echo $result
}

# https://atcoder.jp/contests/arc117/tasks/arc117_a
s=$(sum $array)
array+=$((-s))
echo $array
