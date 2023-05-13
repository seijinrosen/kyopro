N = list(map(int, input()))


even = sum(N[-2::-2])
odd = sum(N[::-2])


print(even, odd)
