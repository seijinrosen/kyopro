from calendar import leapdays

A, B = map(int, input().split())


ans = leapdays(A, B + 1)


print(ans)
