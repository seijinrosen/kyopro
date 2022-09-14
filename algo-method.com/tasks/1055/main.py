N = int(input())
F = list(map(int, input().split()))

ans = sum(1 << f for f in F)
print(ans)
