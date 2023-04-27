N = int(input())


ans = sum((N - 1) // a for a in range(1, N))


print(ans)
