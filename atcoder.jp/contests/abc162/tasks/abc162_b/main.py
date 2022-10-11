N = int(input())
ans = sum(i for i in range(1, N + 1) if i % 3 != 0 if i % 5 != 0)
print(ans)
