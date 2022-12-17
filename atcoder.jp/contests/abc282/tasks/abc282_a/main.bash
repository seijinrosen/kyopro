ascii_uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

read -r K
echo $ascii_uppercase | head -c "$K"
