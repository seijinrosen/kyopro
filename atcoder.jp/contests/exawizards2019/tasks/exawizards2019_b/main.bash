read -r
read -r S

b=$(echo "$S" | tr -cd 'B' | wc -c)
r=$(echo "$S" | tr -cd 'R' | wc -c)

((b < r)) && echo "Yes" || echo "No"
