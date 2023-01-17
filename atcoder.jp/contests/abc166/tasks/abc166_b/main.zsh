read -r N K

arr=()

for ((i = 0; i < K; i++)); do
    read -r _d
    read -A a

    for v in "${a[@]}"; do
        arr+=("$v")
    done
done

st=($(echo "${arr[@]}" | tr " " "\n" | sort --unique))

echo $((N - ${#st[@]}))
