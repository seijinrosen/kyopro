read -r X Y

prize=(300000 200000 100000)
ans=$((prize[X] + prize[Y]))

if ((X == 1 && Y == 1)); then
    ((ans += 400000))
fi

echo $ans
