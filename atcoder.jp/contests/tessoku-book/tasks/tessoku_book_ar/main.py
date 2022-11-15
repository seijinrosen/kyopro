N, Q = map(int, input().split())
QUERIES = [map(int, input().split()) for _ in range(Q)]


def calc_index(x: int) -> int:
    return -x if is_reversed else x - 1


A = list(range(1, N + 1))
is_reversed = False


for query in QUERIES:
    q = next(query)

    if q == 1:
        x, y = query
        A[calc_index(x)] = y

    elif q == 2:
        is_reversed = not is_reversed

    elif q == 3:
        x = next(query)
        print(A[calc_index(x)])
