from itertools import zip_longest

S = input()
T = input()

ans = next(i for i, (s, t) in enumerate(zip_longest(S, T), 1) if s != t)
print(ans)
