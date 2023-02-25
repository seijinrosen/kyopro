from operator import itemgetter

N, *A = map(int, open(0).read().split())


for i, _ in sorted(enumerate(A, start=1), key=itemgetter(1), reverse=True):
    print(i)
