import re

S = input()

result = re.search("^(hi)+$", S)
print("Yes" if result else "No")
