N, K, *H = map(int, open(0).read().split())


ans = sum(sorted(H, reverse=True)[K:])


print(ans)
