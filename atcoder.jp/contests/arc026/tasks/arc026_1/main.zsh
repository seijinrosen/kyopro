min() {
    echo $(($1 < $2 ? $1 : $2))
}

read -r N A B

b=$(min 5 N)
a=$((N - b))
ans=$((A * a + B * b))

echo $ans
