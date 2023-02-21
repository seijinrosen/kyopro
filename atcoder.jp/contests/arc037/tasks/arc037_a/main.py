N, *M = map(int, open(0).read().split())


ans = sum(max(0, 80 - m) for m in M)


print(ans)
