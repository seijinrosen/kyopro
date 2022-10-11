input_int_list = lambda: list(map(int, input().split()))

N, X = input_int_list()
A = input_int_list()


def search(x: int) -> int:
    l = 0
    r = N - 1
    while l <= r:
        m = (l + r) // 2
        if x < A[m]:
            r = m - 1
        if x == A[m]:
            return m
        if x > A[m]:
            l = m + 1
    return -1


ans = search(X)
print(ans + 1)
