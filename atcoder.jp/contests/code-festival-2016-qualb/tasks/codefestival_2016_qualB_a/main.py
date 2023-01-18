S = input()


ans = sum(ch1 != ch2 for ch1, ch2 in zip(S, "CODEFESTIVAL2016"))


print(ans)
