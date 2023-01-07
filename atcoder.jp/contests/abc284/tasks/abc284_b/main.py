T = int(input())

for _ in range(T):
    input()
    A = list(map(int, input().split()))
    ans = sum(a % 2 == 1 for a in A)
    print(ans)
