import re
print(re.sub("\D[^0]\d{5}\D","",input())and"No"or"Yes")