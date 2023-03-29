N, M, *A = map(int, open(0).read().split())


x = sum(A) / (4 * M)
ans = M <= sum(x <= a for a in A)


print("Yes" if ans else "No")
