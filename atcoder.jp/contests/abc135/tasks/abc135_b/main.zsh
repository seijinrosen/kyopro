read -r N
read -A P

cnt=0
for ((i = 1; i <= N; i++)); do
    if ((i != P[i])); then
        ((cnt++))
    fi
done

((cnt == 0 || cnt == 2)) && echo "YES" || echo "NO"
