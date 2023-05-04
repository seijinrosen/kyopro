from collections import Counter

L, R = map(int, input().split())
L_LIST = list(map(int, input().split()))
R_LIST = list(map(int, input().split()))


counter_l = Counter(L_LIST)
counter_r = Counter(R_LIST)
ans = sum(min(l, counter_r[size]) for size, l in counter_l.items())


print(ans)
