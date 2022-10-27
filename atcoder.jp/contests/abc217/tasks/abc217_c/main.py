N = int(input())
P = list(map(int, input().split()))

ans = [0] * N
for i, p in enumerate(P, start=1):
    ans[p - 1] = i

print(*ans)
