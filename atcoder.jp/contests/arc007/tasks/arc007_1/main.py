X = set(input())
S = input()


ans = "".join(ch for ch in S if ch not in X)


print(ans)
