H,W,X,Y,*S=open(0).read().split()
for r in S[int(X)-1:int(X)+2]:print(r[int(Y)-1:int(Y)+2])