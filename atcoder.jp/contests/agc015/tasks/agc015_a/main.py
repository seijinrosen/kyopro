N, A, B = map(int, input().split())


if A == B:
    print(1)
    exit()
elif B < A or N == 1:
    print(0)
    exit()


ans = (B - A) * (N - 2) + 1


print(ans)
