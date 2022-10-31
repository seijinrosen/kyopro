N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = sum(max(0, v - c) for v, c in zip(V, C))
print(ans)
