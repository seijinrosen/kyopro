read -r N

cnt=0
for ((i = 0; i < N; i++)); do
    read -r s

    if [ "$s" = "For" ]; then
        ((cnt++))
    fi
done

((N / 2 < cnt)) && echo "Yes" || echo "No"
