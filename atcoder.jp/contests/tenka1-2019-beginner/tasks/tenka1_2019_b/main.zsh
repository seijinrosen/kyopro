read -r
read -r S
read -r K

echo "$S" | tr -c "${S:$K-1:1}"\\n '*'
