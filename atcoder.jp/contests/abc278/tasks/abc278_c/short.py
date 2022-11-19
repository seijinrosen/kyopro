s={0}
for r in[*open(0)][1:]:
 t,a,b=r.split()
 if"2">t:s|={(a,b)}
 elif"3">t:s-={(a,b)}
 else:print("No"if{(a,b),(b,a)}-s else"Yes")