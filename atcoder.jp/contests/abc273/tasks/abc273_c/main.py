from bisect import bisect_right
from collections import Counter

N = int(input())
A = list(map(int, input().split()))

sorted_set_A = sorted(set(A))
lst = [len(sorted_set_A) - bisect_right(sorted_set_A, a) for a in A]
counter = Counter(lst)

for k in range(N):
    print(counter[k])
