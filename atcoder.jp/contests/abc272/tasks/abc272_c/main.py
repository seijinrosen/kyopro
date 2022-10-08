def even(n: int) -> bool:
    return n % 2 == 0


N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

x = next((A[0] + a for a in A[1:] if even(A[0] + a)), -1)
y = next((A[1] + a for a in A[2:] if even(A[1] + a)), -1)

ans = max(x, y)
print(ans)
