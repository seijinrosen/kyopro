H, W = map(int, input().split())
S = [input() for _ in range(H)]

ans = sum(row.count("o") for row in S)
print(ans)
