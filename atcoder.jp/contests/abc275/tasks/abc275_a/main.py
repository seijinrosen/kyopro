N = int(input())
H = list(map(int, input().split()))

lst = [(h, i) for i, h in enumerate(H, start=1)]
lst.sort(reverse=True)

ans = lst[0][1]
print(ans)
