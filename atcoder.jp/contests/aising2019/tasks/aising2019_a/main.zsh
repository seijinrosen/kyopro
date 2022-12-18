read -r N
read -r H
read -r W

h=$((N - H + 1))
w=$((N - W + 1))

echo $((h * w))
