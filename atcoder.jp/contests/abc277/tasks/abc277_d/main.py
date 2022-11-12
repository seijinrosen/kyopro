N, M = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)
ans = total

top_card = 0
current_sum = 0
card_count = 0

for a in sorted(A) * 2:
    if (a in [top_card, top_card + 1]) or (top_card + 1 == M and a == 0):
        current_sum += a
        card_count += 1
    else:
        current_sum = a
        card_count = 1

    top_card = a
    ans = min(ans, total - current_sum)

    if card_count == N:
        break

print(ans)
