read -r N

for ((i = 0; i < N; i++)); do
    read -r s t
    S[i]=$s
    T[i]=$t
done

read -r X

ans=0
asleep=false

for ((i = 0; i < N; i++)); do
    if $asleep; then
        ((ans += T[i]))
    fi
    if [ "${S[i]}" == "$X" ]; then
        asleep=true
    fi
done

echo $ans
