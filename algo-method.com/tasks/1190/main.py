N = int(input())
S = input()
T = input()

ans = bin(int(S, 2) * int(T, 2))[2:].zfill(N)[-N:]
print(ans)
