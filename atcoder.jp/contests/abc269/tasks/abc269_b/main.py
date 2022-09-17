S = [input() for _ in range(10)]

ab = [i for i, s in enumerate(S) if "#" in s]
cd = [i for i, c in enumerate(S[ab[0]]) if c == "#"]

a = ab[0] + 1
b = ab[-1] + 1
c = cd[0] + 1
d = cd[-1] + 1

print(a, b)
print(c, d)
