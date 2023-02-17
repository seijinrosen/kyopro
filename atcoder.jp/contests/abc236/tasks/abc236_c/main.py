N, M = map(int, input().split())
S = input().split()
T = input().split()


st = set(T)
for s in S:
    print("Yes" if s in st else "No")
