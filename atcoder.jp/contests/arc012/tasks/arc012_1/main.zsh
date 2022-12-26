read -r day

if [ "$day" = "Monday" ]; then
    echo 5
elif [ "$day" = "Tuesday" ]; then
    echo 4
elif [ "$day" = "Wednesday" ]; then
    echo 3
elif [ "$day" = "Thursday" ]; then
    echo 2
elif [ "$day" = "Friday" ]; then
    echo 1
else
    echo 0
fi
