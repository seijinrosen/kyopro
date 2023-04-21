N, *A = map(int, open(0).read().split())


ans = [0] * N
for a in A:
    ans[a - 1] += 1


print(*ans, sep="\n")
