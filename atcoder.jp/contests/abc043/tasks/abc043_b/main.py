S = input()

lst: "list[str]" = []

for s in S:
    if s in {"0", "1"}:
        lst.append(s)
    elif s == "B" and lst:
        lst.pop()

ans = "".join(lst)
print(ans)
