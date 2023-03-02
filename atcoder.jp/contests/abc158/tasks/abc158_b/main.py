N, A, B = map(int, input().split())


ab = A + B
ans = (N // ab) * A + min(A, N % ab)


print(ans)
