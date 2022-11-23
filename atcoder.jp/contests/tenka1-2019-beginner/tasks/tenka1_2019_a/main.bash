read -r A B C

if ((A < C && C < B)) || ((B < C && C < A)); then
    ans="Yes"
else
    ans="No"
fi

echo $ans
