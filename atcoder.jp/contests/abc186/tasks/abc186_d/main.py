from itertools import accumulate

N, *A = map(int, open(0).read().split())


A.sort()
acc = [0, *accumulate(A)]
ans = sum(i * a - acc[i] for i, a in enumerate(A))


print(ans)
