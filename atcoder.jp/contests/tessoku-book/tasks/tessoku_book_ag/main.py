from functools import reduce
from operator import xor

N = int(input())
A = list(map(int, input().split()))

nim = reduce(xor, A)
print("First" if nim != 0 else "Second")
