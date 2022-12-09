result=$(grep -E "^(hi)+$" | wc -c)
((result == 0)) && echo "No" || echo "Yes"
