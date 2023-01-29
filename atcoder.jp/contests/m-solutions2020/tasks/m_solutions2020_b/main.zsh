read -r a b c
read -r K

for ((i = 0; i <= K; i++)); do
    if ((a < b && b < c)); then
        echo "Yes"
        exit 0
    fi

    if ((a >= b)); then
        ((b *= 2))
    elif ((b >= c)); then
        ((c *= 2))
    fi
done

echo "No"
