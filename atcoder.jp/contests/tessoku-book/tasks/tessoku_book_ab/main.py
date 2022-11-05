N = int(input())

now = 0

for _ in range(N):
    t, a = input().split()
    a = int(a)

    if t == "+":
        now += a
    elif t == "-":
        now -= a
    elif t == "*":
        now *= a

    now %= 10000
    print(now)
