N, *S = open(0).read().split()


T = sorted("indeednow")


for s in S:
    print("YES" if sorted(s) == T else "NO")
