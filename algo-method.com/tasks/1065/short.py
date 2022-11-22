H,W,X,Y=map(int,input().split())
for r in[input()for _ in range(H)][X-1:X+2]:print(r[Y-1:Y+2])