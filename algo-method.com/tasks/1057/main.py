N = int(input())

ans = [i for i in range(30) if N & 1 << i]

print(len(ans))
print(*ans)
