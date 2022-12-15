is_product_day() {
    local m=$1
    local d=$2
    local d10=$((d / 10))
    local d1=$((d % 10))
    echo $((d1 >= 2 && d10 >= 2 && d1 * d10 <= m))
}

read -r M D

ans=0
for ((d = 1; d <= D; d++)); do
    if (($(is_product_day "$M" $d))); then
        ((ans++))
    fi
done

echo $ans
