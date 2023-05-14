N, A, B, *C = map(int, open(0).read().split())


ans = C.index(A + B) + 1


print(ans)
