def solve(n: int) -> bool:
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    return n % 4 == 0


N = int(input())

ans = "Yes" if solve(N) else "No"

print(ans)
