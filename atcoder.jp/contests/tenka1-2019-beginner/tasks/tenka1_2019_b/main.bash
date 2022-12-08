read -r N
read -r S
read -r K

for ((i = 0; i < N; i++)); do
    c=${S:i:1}
    if [ "$c" == "${S:K-1:1}" ]; then
        ans+="$c"
    else
        ans+='*'
    fi
done

echo "$ans"
