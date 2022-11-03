from functools import partial
from operator import mul

X, Y = map(int, input().split())

ans = 4 * X - Y in map(partial(mul, 2), range(X + 1))

print("Yes" if ans else "No")
