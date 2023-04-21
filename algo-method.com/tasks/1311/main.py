S = input()


ans = len({S[i : i + 3] for i in range(len(S) - 2)})


print(ans)
