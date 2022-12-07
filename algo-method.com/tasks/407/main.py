from typing import Callable


def meguru(pred: Callable[[int], bool], ok: int, ng: int) -> int:
    """めぐる式二分探索
    最大値を求める場合: ok < ng
    最小値を求める場合: ok > ng
    """
    while 1 < abs(ok - ng):
        mid = (ok + ng) // 2
        if pred(mid):
            ok = mid
        else:
            ng = mid
    return ok


N, X = map(int, input().split())


def pred(k: int) -> bool:
    return X <= sum(min(N, k // i) for i in range(1, N + 1))


ans = meguru(pred, ok=N**2, ng=0)
print(ans)
