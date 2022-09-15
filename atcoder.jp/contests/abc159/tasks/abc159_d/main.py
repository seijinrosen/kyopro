from collections import Counter

N = int(input())
A = list(map(int, input().split()))


def nC2(n: int) -> int:
    if n < 2:
        return 0
    return n * (n - 1) // 2


counter = Counter(A)
total = sum(map(nC2, counter.values()))

ans_list = [total - nC2(counter[a]) + nC2(counter[a] - 1) for a in A]
print(*ans_list, sep="\n")
