N, *A = map(int, open(0).read().split())


ans = [a for a in A if a % 2 == 0]


print(*ans)
