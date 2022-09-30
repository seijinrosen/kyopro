X = int(input())

coin500 = X // 500
coin5 = X % 500 // 5

ans = 1000 * coin500 + 5 * coin5
print(ans)
