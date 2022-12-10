import re
print("Yes"if re.match(r"\D[1-9]\d{5}\D",input())else"No")