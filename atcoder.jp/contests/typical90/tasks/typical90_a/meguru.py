from typing import Callable


def meguru(pred: Callable[[int], bool], ok: int, ng: int) -> int:
    while 1 < abs(ok - ng):
        mid = (ok + ng) // 2
        if pred(mid):
            ok = mid
        else:
            ng = mid
    return ok


N, L, K, *A = map(int, open(0).read().split())


def pred(score: int) -> bool:
    k = 0
    now = 0
    for a in A:
        if score <= a - now and score <= L - a:
            k += 1
            now = a
    return K <= k


ans = meguru(pred, ok=1, ng=L)
print(ans)
