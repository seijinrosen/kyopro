N = int(input())


ans = next((str(i) for i in range(1, N + 1) if int(i * 1.08) == N), ":(")


print(ans)
