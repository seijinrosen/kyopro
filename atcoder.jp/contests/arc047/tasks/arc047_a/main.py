N, L = map(int, input().split())
S = input()


now = 1
ans = 0

for ch in S:
    if ch == "+":
        now += 1
        if L < now:
            ans += 1
            now = 1
    elif ch == "-":
        now -= 1


print(ans)
