S = input()

X = "WBWBWWBWBWBW" * 2
Y = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "So", "So#", "La", "La#", "Si"]

dict_ = {X[i : i + 12]: Y[i] for i in range(12)}
ans = dict_[S[:12]]

print(ans)
