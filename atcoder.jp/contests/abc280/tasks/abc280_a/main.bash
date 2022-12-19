count() {
    tr -cd "$1" | wc -c
}

read -r H _

ans=0
for ((i = 0; i < H; i++)); do
    ((ans += $(count '#')))
done

echo $ans
