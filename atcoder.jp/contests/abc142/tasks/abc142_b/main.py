input_int_list = lambda: list(map(int, input().split()))
N, K = input_int_list()
H = input_int_list()

ans = sum(K <= h for h in H)
print(ans)
