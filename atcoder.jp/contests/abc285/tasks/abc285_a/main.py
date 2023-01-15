a, b = map(int, input().split())


ans = b in {2 * a, 2 * a + 1}


print("Yes" if ans else "No")
