read -r _N
read -A A

max=0
min=10000

for item in "${A[@]}"; do
    if ((max < item)); then
        max=$item
    fi
    if ((item < min)); then
        min=$item
    fi
done

echo $((max - min))
