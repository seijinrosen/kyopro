from itertools import dropwhile
from operator import itemgetter
from typing import Tuple


def input_st() -> Tuple[str, int]:
    s, t = input().split()
    return s, int(t)


N = int(input())
ST = [input_st() for _ in range(N)]
X = input()

it = dropwhile(lambda st: st[0] != X, ST)
next(it)
ans = sum(map(itemgetter(1), it))

print(ans)
