read -r S

if ((${#S} == 2)); then
    ans=$S
else
    ans=$(echo "$S" | rev)
fi

echo "$ans"
