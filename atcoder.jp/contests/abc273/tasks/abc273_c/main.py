from collections import Counter

N = int(input())
A = list(map(int, input().split()))

counter = sorted(Counter(A).items(), reverse=True)
ans = [v for _, v in counter] + [0] * (N - len(counter))

print(*ans, sep="\n")
