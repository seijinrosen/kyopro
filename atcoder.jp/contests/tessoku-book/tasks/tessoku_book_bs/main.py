from operator import mul

N = int(input())
A = map(int, input().split())
B = map(int, input().split())

ans = sum(map(mul, sorted(A), sorted(B, reverse=True)))
print(ans)
