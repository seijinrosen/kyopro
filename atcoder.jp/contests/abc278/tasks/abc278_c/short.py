s={0}
for r in[*open(0)][1:]:
 t,a,b=map(int,r.split())
 if t<2:s|={(a,b)}
 elif t<3:s-={(a,b)}
 else:print("No"if{(a,b),(b,a)}-s else"Yes")