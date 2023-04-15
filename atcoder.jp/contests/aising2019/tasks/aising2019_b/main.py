N, A, B, *P = map(int, open(0).read().split())


a = [p for p in P if p <= A]
b = [p for p in P if A + 1 <= p <= B]
c = [p for p in P if B + 1 <= p]
ans = min(map(len, (a, b, c)))


print(ans)
