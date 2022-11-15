S="WBR"
N,C,A=open(0).read().split()
print("YNeos"[sum(map(S.find,A))%3!=S.find(C)::2])