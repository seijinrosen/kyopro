from bisect import*
N,C,Q,*X=open(s:=0)
S=[s:=s+c for c in sorted(map(int,C.split()))]
for x in X:print(bisect(S,int(x)))