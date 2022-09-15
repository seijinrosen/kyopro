from collections import Counter

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
BC: "list[tuple[int, int]]" = [tuple(map(int, input().split())) for _ in range(Q)]

s = sum(A)
counter = Counter(A)
ans_list = [0] * Q

for i, (b, c) in enumerate(BC):
    s += (c - b) * counter[b]
    counter[c] += counter[b]
    counter[b] = 0
    ans_list[i] = s

print(*ans_list, sep="\n")
