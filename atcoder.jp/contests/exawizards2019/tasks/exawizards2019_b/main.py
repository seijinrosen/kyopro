N = int(input())
S = input()

ans = S.count("B") < S.count("R")
print("Yes" if ans else "No")
