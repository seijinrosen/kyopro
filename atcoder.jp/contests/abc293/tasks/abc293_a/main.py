S = input()


ans = "".join(S[i + 1] + S[i] for i in range(0, len(S), 2))


print(ans)
