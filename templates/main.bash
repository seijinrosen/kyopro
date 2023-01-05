# https://atcoder.jp/contests/abc282/tasks/abc282_a
ascii_uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
echo $ascii_uppercase | head -c "$K"

abs() {
    if ((0 <= $1)); then
        echo "$1"
    else
        echo "${1:1}"
    fi
}
count() {
    tr -cd "$1" | wc -c
}
div_ceil() {
    echo $((($1 + $2 - 1) / $2))
}
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
is_palindrome() {
    (($1)) && echo $(($(echo "$1" | rev) == $1)) || echo 1
}
# len(S)
# ${#S}
max() {
    echo $(($1 < $2 ? $2 : $1))
}
min() {
    echo $(($1 < $2 ? $1 : $2))
}
rstrip() {
    local s=$1
    local c=$2
    local n=${#s}
    for ((i = n - 1; i >= 0; i--)); do
        if ((${s:i:1} != c)); then
            break
        fi
        ((n--))
    done
    echo "${s:0:n}"
}
string_set_len() {
    echo "$1" | fold -w1 | sort --unique | wc -l
}
sum() {
    local result=0
    for x in $1; do
        ((result += x))
    done
    echo $result
}
yes_no() {
    (($1)) && echo "Yes" || echo "No"
}

echo $(($(div_ceil "$Y"*"$Z" "$X") - 1))

read -r N
read -ra A

for ((i = 0; i < N; i++)); do
    read -r s t
    S[i]=$s
    T[i]=$t
done

ans=$((10 - N / 200))

for ((i = 0; i < N; i += 2)); do
    if ((A[i] % 2 == 1)); then
        ((ans++))
    fi
done

for ((i = 0; i < N; i++)); do
    if $asleep; then
        ((ans += T[i]))
    fi
    if [ "${S[i]}" == "$X" ]; then
        asleep=true
    fi
done

prize=(0 300000 200000 100000)
ans=$((prize[X] + prize[Y]))
if ((X == 1 && Y == 1)); then
    ((ans += 400000))
fi

# ABCD=$(tr " " "\n" | sort -n)
# array=($ABCD)
# A=${array[0]}
# B=${array[1]}
# C=${array[2]}
# D=${array[3]}
ans=$((A + B + C == D || A + D == B + C))
((ans)) && echo "Yes" || echo "No"

N=$(tr " " "\n" | sort -n | tr -d "\n")
[ "$N" == "1479" ] && echo "YES" || echo "NO"

read -r S
if ((${#S} == 2)); then
    ans=$S
else
    ans=$(echo "$S" | rev)
fi

b=$(echo "$S" | tr -cd 'B' | wc -c)
r=$(echo "$S" | tr -cd 'R' | wc -c)
((b < r)) && echo "Yes" || echo "No"

read -r A
read -r B
x=$((B * 5))
# 数値 x と 文字列 A を文字列として連結
x+=$A

echo "$S" | tr -c "${S:K-1:1}"\\n '*'

result=$(grep -E "^(hi)+$" | wc -c)
((result == 0)) && echo "No" || echo "Yes"

grep -Eq "^[A-Z][^0][0-9]{5}[A-Z]$" && echo "Yes" || echo "No"

# https://atcoder.jp/contests/abc281/tasks/abc281_a
seq "$N" -1 0

# https://atcoder.jp/contests/m-solutions2019/tasks/m_solutions2019_b
(($(tr -cd 'x' | wc -c) <= 7)) && echo "YES" || echo "NO"

# https://atcoder.jp/contests/jsc2019-qual/tasks/jsc2019_qual_a
is_product_day() {
    local m=$1
    local d=$2
    local d10=$((d / 10))
    local d1=$((d % 10))
    echo $((d1 >= 2 && d10 >= 2 && d1 * d10 <= m))
}
for ((d = 1; d <= D; d++)); do
    if (($(is_product_day "$M" $d))); then
        ((ans++))
    fi
done

# https://atcoder.jp/contests/arc117/tasks/arc117_a
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

# https://atcoder.jp/contests/abc164/tasks/abc164_c
sort --unique | wc -l

# https://atcoder.jp/contests/abc212/tasks/abc212_b
is_weak2() {
    local flag=1
    for ((i = 0; i < 3; i++)); do
        local x=${1:i:1}
        local y=${1:i+1:1}
        if (((x + 1) % 10 != y)); then
            flag=0
            break
        fi
    done
    echo $flag
}
