A=[*open(0)][1].split()
print(sum(c*(c-1)*(c-2)//6for c in[A.count(str(i))for i in range(101)]))