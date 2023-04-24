from itertools import product

N = int(input())


diff = 2025 - N
ans = [f"{i} x {j}" for i, j in product(range(1, 10), repeat=2) if i * j == diff]


print(*ans, sep="\n")
