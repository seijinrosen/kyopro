N = int(input())
A = input()
B = input()
C = input()


ans = sum(len({a, b, c}) - 1 for a, b, c in zip(A, B, C))


print(ans)
