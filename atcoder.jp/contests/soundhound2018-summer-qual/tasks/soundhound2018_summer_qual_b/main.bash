read -r S
read -r w

ans=""
for ((i = 0; i < ${#S}; i += w)); do
    ans+=${S:i:1}
done

echo "$ans"
