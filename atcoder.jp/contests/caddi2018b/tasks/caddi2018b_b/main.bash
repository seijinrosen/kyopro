read -r N H W

ans=0
for ((i = 0; i < N; i++)); do
    read -r a b
    if ((H <= a && W <= b)); then
        ((ans++))
    fi
done

echo $ans
