N, Q = map(int, input().split())
LA = [list(map(int, input().split())) for _ in range(N)]
ST: "list[tuple[int, int]]" = [tuple(map(int, input().split())) for _ in range(Q)]

for s, t in ST:
    print(LA[s - 1][t])
