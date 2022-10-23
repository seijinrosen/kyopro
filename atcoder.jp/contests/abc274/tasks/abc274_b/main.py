H, W = map(int, input().split())
C = [input() for _ in range(H)]

ans = [row.count("#") for row in zip(*C)]
print(*ans)
