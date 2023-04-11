S = input()


ans = min(abs(int(S[i : i + 3]) - 753) for i in range(len(S) - 2))


print(ans)
