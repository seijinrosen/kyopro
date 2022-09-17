from itertools import compress, product
from typing import Iterator

N = int(input())

b = list(bin(N)[2:])
idx = [i for i, c in enumerate(b) if c == "1"]


def bitset(n: int) -> Iterator["tuple[int, ...]"]:
    for bits in product((0, 1), repeat=n):
        yield bits


for bits in bitset(len(idx)):
    x = compress(idx, bits)
    y = ["0"] * len(b)
    for z in x:
        y[z] = "1"

    print(int("".join(y), 2))
