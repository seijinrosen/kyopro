read -r a b

if ((a + b == 15)); then
    ans="+"
elif ((a * b == 15)); then
    ans="*"
else
    ans="x"
fi

echo "$ans"
