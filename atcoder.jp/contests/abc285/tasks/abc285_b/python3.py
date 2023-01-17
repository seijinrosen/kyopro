N = int(input())
S = input()


for i in range(1, N):
    l = 0

    for x, y in zip(S, S[i:]):
        if x == y:
            break
        l += 1

    print(l)
