S="WBR"
print("YNeos"[input()[-1]!=S[sum(map(S.find,input()))%3]::2])