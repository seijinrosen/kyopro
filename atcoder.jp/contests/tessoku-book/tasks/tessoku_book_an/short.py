from collections import Counter
print(sum(a*(a-1)*(a-2)//6for a in Counter(map(int,[*open(0)][1].split())).values()))