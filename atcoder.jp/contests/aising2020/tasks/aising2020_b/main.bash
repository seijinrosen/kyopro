read -r N
read -ra A

ans=0
for ((i = 0; i < N; i += 2)); do
    if ((A[i] % 2 == 1)); then
        ((ans++))
    fi
done

echo "$ans"
