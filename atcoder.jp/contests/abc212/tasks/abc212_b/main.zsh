string_set_len() {
    echo "$1" | fold -w1 | sort --unique | wc -l
}

is_weak1() {
    echo $(($(string_set_len "$1") == 1))
}

is_weak2() {
    local flag=1
    for ((i = 0; i < 3; i++)); do
        local x=${1:$i:1}
        local y=${1:$i+1:1}
        if (((x + 1) % 10 != y)); then
            flag=0
            break
        fi
    done
    echo $flag
}

read -r XS
(($(is_weak1 "$XS") || $(is_weak2 "$XS"))) && echo "Weak" || echo "Strong"
