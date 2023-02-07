N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))


ans = 0
pre = -1000

for a in A:
    a -= 1
    ans += B[a]
    if a == pre + 1:
        ans += C[pre]
    pre = a


print(ans)
