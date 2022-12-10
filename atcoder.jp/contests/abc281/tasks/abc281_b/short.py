import re
print("Yes"if re.match(r"\D[^0]\d{5}\D",input())else"No")