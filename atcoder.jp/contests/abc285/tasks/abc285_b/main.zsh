read -r N
read -r S

for ((i = 1; i < N; i++)); do
    l=0

    for ((k = 0; k < N - i; k++)); do
        if [ "${S:$k:1}" = "${S:$k+$i:1}" ]; then
            break
        fi

        ((l++))
    done

    echo $l
done
