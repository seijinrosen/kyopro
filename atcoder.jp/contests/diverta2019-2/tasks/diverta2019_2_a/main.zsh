read -r N K

ans=$((K == 1 ? 0 : N - K))
echo $ans
