from functools import partial

K = int(input())
A, B = map(partial(int, base=K), input().split())

ans = A * B
print(ans)
