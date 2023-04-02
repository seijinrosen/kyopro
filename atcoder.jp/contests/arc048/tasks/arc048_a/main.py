A, B = map(int, input().split())


ans = B - A - (A < 0 and 0 < B)


print(ans)
