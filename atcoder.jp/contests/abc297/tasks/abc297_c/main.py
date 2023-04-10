H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]


for row in S:
    for j in range(W - 1):
        if row[j] == "T" and row[j + 1] == "T":
            row[j] = "P"
            row[j + 1] = "C"


for row in S:
    print("".join(row))
