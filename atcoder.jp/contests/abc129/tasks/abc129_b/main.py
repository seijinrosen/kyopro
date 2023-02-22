from itertools import accumulate

N, *W = map(int, open(0).read().split())


acc = list(accumulate(W))
ans = min(abs(acc[-1] - 2 * s) for s in acc)


print(ans)
