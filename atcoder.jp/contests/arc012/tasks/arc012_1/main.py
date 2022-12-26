def solve(day: str) -> int:
    if day in {"Sunday", "Saturday"}:
        return 0
    return 5 - ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"].index(day)


print(solve(input()))
