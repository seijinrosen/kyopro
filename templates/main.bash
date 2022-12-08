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
echo $ans

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
