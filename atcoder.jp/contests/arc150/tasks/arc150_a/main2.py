from itertools import accumulate

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    S = input()

    acc_1 = [0, *accumulate(int(c == "1") for c in S)]
    acc_0 = [0, *accumulate(int(c == "0") for c in S)]

    ok = sum(
        acc_1[i + K] - acc_1[i] == acc_1[N] and acc_0[i + K] == acc_0[i]
        for i in range(N - K + 1)
    )

    print("Yes" if ok == 1 else "No")
