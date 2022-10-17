N=int(input());A=[*map(int,input().split())];B=[*map(int,input().split())];d=[0,A[0]]
for i in range(2,N):d.append(min(d[i-1]+A[i-1],d[i-2]+B[i-2]))
print(d[-1])