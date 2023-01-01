N = int(input())
A = list(map(int, input().split()))

ans = len(set(A)) == N

print("YES" if ans else "NO")
