N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = sorted(set(A) ^ set(B))
print(*ans)
