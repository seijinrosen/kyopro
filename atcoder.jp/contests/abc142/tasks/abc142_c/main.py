from operator import itemgetter

N, *A = map(int, open(0).read().split())


ans = [i for i, _ in sorted(enumerate(A, 1), key=itemgetter(1))]


print(*ans)
