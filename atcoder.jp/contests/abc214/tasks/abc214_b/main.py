S, T = map(int, input().split())

ans = sum(
    a * b * c <= T
    for a in range(S + 1)
    for b in range(S - a + 1)
    for c in range(S - a - b + 1)
)

print(ans)
