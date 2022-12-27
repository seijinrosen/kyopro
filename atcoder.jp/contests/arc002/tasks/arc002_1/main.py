def is_leap(y: int) -> bool:
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    return y % 4 == 0


print("YES" if is_leap(int(input())) else "NO")
