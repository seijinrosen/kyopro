N, *S = open(0).read().split()


ans = int(N) // 2 < S.count("For")


print("Yes" if ans else "No")
