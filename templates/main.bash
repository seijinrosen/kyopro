read -r N
read -ra A
for ((i = 0; i < N; i++)); do
    read -r s t
    S[i]=$s
    T[i]=$t
done

ans=$((10 - N / 200))
echo $ans

ans=0
for ((i = 0; i < N; i += 2)); do
    if ((A[i] % 2 == 1)); then
        ((ans++))
    fi
done

echo "$ans"

for ((i = 0; i < N; i++)); do
    if $asleep; then
        ((ans += T[i]))
    fi
    if [ "${S[i]}" == "$X" ]; then
        asleep=true
    fi
done

# tr
# wc
