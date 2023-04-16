from collections import Counter
from typing import Tuple


def convert_input(input_str: str) -> Tuple[int, str]:
    n, s = input_str.split()
    return int(n), s


N, S = convert_input(input())


ans = 0
for i, si in enumerate(S):
    counter = Counter(si)
    for sj in S[i + 1 :]:
        counter[sj] += 1
        if counter["A"] == counter["T"] and counter["C"] == counter["G"]:
            ans += 1


print(ans)
