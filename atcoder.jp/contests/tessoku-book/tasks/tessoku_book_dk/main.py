from itertools import accumulate

N = int(input())
S = input()

ret1 = [*accumulate(S, lambda x, y: x + 1 if y == "A" else 1, initial=1)]
ret2 = [*accumulate(S[::-1], lambda x, y: x + 1 if y == "B" else 1, initial=1)][::-1]

ans = sum(map(max, ret1, ret2))
print(ans)
