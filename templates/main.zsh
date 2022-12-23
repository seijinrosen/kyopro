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
