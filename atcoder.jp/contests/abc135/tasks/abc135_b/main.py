N = int(input())
P = list(map(int, input().split()))

cnt = sum(i != p for i, p in enumerate(P, start=1))
ans = cnt in {0, 2}

print("YES" if ans else "NO")
