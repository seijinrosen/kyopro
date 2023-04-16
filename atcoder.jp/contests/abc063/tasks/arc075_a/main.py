N, *S = map(int, open(0).read().split())


total = sum(S)
ans = (
    total - min((s for s in S if s % 10 != 0), default=total)
    if total % 10 == 0
    else total
)


print(ans)
