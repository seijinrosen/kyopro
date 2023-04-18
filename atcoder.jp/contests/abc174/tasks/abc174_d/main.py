N = int(input())
C = list(input())


def solve() -> int:
    ret = 0
    right = N

    for left in range(N):
        if C[left] == "W":
            while left < right:
                right -= 1
                if C[right] == "R":
                    ret += 1
                    C[left], C[right] = C[right], C[left]
                    break

    return ret


ans = solve()


print(ans)
