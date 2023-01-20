read -r N
read -ra P

cnt=0
for ((i = 0; i < N; i++)); do
    if ((i + 1 != P[i])); then
        ((cnt++))
    fi
done

((cnt == 0 || cnt == 2)) && echo "YES" || echo "NO"
