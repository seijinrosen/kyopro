from itertools import accumulate
from operator import sub

N = int(input())
A = list(map(int, input().split()))

ans = sum(map(sub, accumulate(A, max), A))
print(ans)
