N = int(input())
S = input()


for i in range(1, N):
    l = 0

    for k in range(N - i):
        if S[k] == S[k + i]:
            break
        l += 1

    print(l)
