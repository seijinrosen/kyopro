x=42
while ((x <= 130000000)); do
    ((x *= 2))
done

echo $x
