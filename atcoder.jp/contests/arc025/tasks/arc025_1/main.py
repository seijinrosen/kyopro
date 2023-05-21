D = list(map(int, input().split()))
J = list(map(int, input().split()))


ans = sum(map(max, D, J))


print(ans)
