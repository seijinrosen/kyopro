def mod_index1(x: int, y: int) -> int:
    return (x - 1) % y + 1


N = int(input())

G = [(i, mod_index1(i + 1, N)) for i in range(1, N + 1)]

print(N)
for g in G:
    print(*g)
