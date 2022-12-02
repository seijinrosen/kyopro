N=$(tr " " "\n" | sort -n | tr -d "\n")
[ "$N" == "1479" ] && echo "YES" || echo "NO"
