import re
print("Yes"if re.match("\D[^0]\d{5}\D",input())else"No")