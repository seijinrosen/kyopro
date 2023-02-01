read -r a b K

for ((i = 0; i < K; i++)); do
    if ((i % 2 == 0)); then
        ((b += a / 2))
        ((a /= 2))
    else
        ((a += b / 2))
        ((b /= 2))
    fi
done

echo "$a" "$b"
