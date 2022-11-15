N,C=input().split()
A=input()
s="WBR"
print("YNeos"[sum(map(s.index,A))%3!=s.find(C)::2])