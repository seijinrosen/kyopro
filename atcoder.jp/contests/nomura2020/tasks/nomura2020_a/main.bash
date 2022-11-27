read -r H1 M1 H2 M2 K

ans=$((60 * (H2 - H1) + M2 - M1 - K))
echo $ans
