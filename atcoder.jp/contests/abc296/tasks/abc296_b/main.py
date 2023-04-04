from itertools import product
from string import ascii_lowercase

S = [input() for _ in range(8)]


ans = next(
    ascii_lowercase[j] + str(8 - i)
    for i, j in product(range(8), repeat=2)
    if S[i][j] == "*"
)


print(ans)
