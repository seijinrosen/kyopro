from string import ascii_uppercase

N = int(input())
S = input()


ans = S.translate(
    str.maketrans(
        {ch: ascii_uppercase[i % 26] for i, ch in enumerate(ascii_uppercase, N)}
    )
)


print(ans)
