N = int(input())
A = list(map(int, input().split()))

ans = sorted(A)[-2]
print(ans)
