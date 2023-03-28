N, *A = map(int, open(0).read().split())


lst = [False] * N
for i, a in enumerate(A):
    if not lst[i]:
        lst[a - 1] = True


ans = [i for i, x in enumerate(lst, 1) if not x]


print(len(ans))
print(*ans)
