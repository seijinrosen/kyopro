S="WBR"
print("YNeos"[S.find(input()[-1])!=sum(map(S.find,input()))%3::2])