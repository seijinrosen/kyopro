read -r N P Q R S
read -A A

ans=()

for ((i = 1; i < P; i++)); do
    ans+=("${A[i]}")
done

for ((i = R; i <= S; i++)); do
    ans+=("${A[i]}")
done

for ((i = Q + 1; i < R; i++)); do
    ans+=("${A[i]}")
done

for ((i = P; i <= Q; i++)); do
    ans+=("${A[i]}")
done

for ((i = S + 1; i <= N; i++)); do
    ans+=("${A[i]}")
done

echo "${ans[@]}"
