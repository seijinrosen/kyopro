A, B, C = map(int, input().split())


def solve() -> str:
    if C % 2 == 0:
        if abs(A) < abs(B):
            return "<"
        if abs(A) > abs(B):
            return ">"
        return "="
    if A < B:
        return "<"
    if A > B:
        return ">"
    return "="


print(solve())
