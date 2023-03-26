N, *W = open(0).read().split()


words = {"and", "not", "that", "the", "you"}
ans = any(w in words for w in W)


print("Yes" if ans else "No")
