N, M = map(int, input().split())
A = [int(x) - 1 for x in input().split()]

B = list(range(N))
for a in A:
    B[a], B[a + 1] = B[a + 1], B[a]

pos = [0] * N
for i, b in enumerate(B):
    pos[b] = i

C = list(range(N))

for a in A:
    if C[a] == 0:
        k = C[a + 1]
    elif C[a + 1] == 0:
        k = C[a]
    else:
        k = 0

    j = pos[k]
    print(j + 1)

    C[a], C[a + 1] = C[a + 1], C[a]
