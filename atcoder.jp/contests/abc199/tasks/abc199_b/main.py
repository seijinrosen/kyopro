N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = max(0, min(B) - max(A) + 1)
print(ans)
