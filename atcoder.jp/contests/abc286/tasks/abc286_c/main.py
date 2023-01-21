from collections import deque

N, A, B = map(int, input().split())
S = input()


ans = 0


for i in range(N // 2):
    left = S[i]
    right = S[N - i - 1]
    if left != right:
        ans += B


que = deque(S)


for i in range(N - 1):
    que.append(que.popleft())
    tmp = (i + 1) * A

    for j in range(N // 2):
        left = que[j]
        right = que[N - j - 1]
        if left != right:
            tmp += B

    ans = min(ans, tmp)


print(ans)
