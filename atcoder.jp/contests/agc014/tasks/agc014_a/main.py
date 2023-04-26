a, b, c = map(int, input().split())


ans = 0
while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    ans += 1

    aa = a // 2
    bb = b // 2
    cc = c // 2

    a = bb + cc
    b = aa + cc
    c = aa + bb

    if 10**5 < ans:
        ans = -1
        break


print(ans)
