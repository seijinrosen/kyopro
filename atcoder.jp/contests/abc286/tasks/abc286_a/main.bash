read -r N P Q R S
read -ra A

ans=()

for ((i = 0; i < P - 1; i++)); do
    ans+=("${A[i]}")
done

for ((i = R - 1; i < S; i++)); do
    ans+=("${A[i]}")
done

for ((i = Q; i < R - 1; i++)); do
    ans+=("${A[i]}")
done

for ((i = P - 1; i < Q; i++)); do
    ans+=("${A[i]}")
done

for ((i = S; i < N; i++)); do
    ans+=("${A[i]}")
done

echo "${ans[@]}"
