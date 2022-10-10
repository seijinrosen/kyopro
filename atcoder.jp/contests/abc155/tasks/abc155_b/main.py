N = int(input())
A = map(int, input().split())

ans = all(a % 3 == 0 or a % 5 == 0 for a in A if a % 2 == 0)
print("APPROVED" if ans else "DENIED")
