from operator import sub

N = int(input())
A = map(int, input().split())
B = map(int, input().split())

ans = sum(map(abs, map(sub, sorted(A), sorted(B))))
print(ans)
