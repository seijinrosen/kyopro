read -r S
T="CODEFESTIVAL2016"

ans=0
for ((i = 0; i < 16; i++)); do
    if [ "${S:$i:1}" != ${T:$i:1} ]; then
        ((ans++))
    fi
done

echo $ans
