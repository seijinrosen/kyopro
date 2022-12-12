div_ceil() {
    echo $((($1 + $2 - 1) / $2))
}

read -r X Y Z
echo $(($(div_ceil "$Y"*"$Z" "$X") - 1))
