from collections import Counter


def prime_factorize(n: int) -> "Counter[int]":
    """素因数分解"""
    counter: Counter[int] = Counter()
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            e += 1
            n //= p
        if e != 0:
            counter[p] = e
        p += 1
    if n != 1:
        counter[n] = 1
    return counter


# input functions --------------------------------------------------------------
def input_int_list() -> "list[int]":
    return list(map(int, input().split()))


def main() -> None:
    _N = int(input())
    A = input_int_list()

    ans = min(prime_factorize(a)[2] for a in A)
    print(ans)


main()
