from typing import List, Tuple

N = int(input())
AB: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N)]


AB.sort(key=lambda x: x[0] * 2 + x[1], reverse=True)
a_sum = sum(a for a, _ in AB)
b_sum = 0
ans = 0
for a, b in AB:
    a_sum -= a
    b_sum += a + b
    ans += 1
    if a_sum < b_sum:
        break


print(ans)
