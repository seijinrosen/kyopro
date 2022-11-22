from operator import itemgetter

H, W, X, Y = map(int, input().split())
S = [input() for _ in range(H)]

ans = map(itemgetter(slice(Y - 1, Y + 2)), S[X - 1 : X + 2])
print(*ans, sep="\n")
