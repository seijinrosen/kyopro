read -r
read -ra H

current=0
ans=0

for h in "${H[@]}"; do
    if ((current <= h)); then
        current=$h
        ((ans++))
    fi
done

echo $ans
