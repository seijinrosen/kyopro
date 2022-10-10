from itertools import groupby


def run_length_encoding(s: str) -> "list[tuple[str, int]]":
    return [(k, len(list(g))) for k, g in groupby(s)]


T = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    s = input()

    run_length = run_length_encoding(s)
    one_indexes = [i for i, (ch, _) in enumerate(run_length) if ch == "1"]

    if len(one_indexes) == 0:
        # "1" が含まれない
        if (
            sum(ch == "?" and cnt >= k for ch, cnt in run_length) == 1
            and sum(ch == "?" and cnt == k for ch, cnt in run_length) == 1
        ):
            print("Yes")
        else:
            print("No")
    elif len(one_indexes) == 1:
        # "1" の連続が 1 つだけ含まれる
        one_index = one_indexes[0]
        one_cnt = run_length[one_index][1]

        if one_cnt > k:
            print("No")
        elif one_cnt == k:
            print("Yes")
        elif one_index == 0:
            right = run_length[1]
            if right[0] == "0":
                print("No")
            elif one_cnt + right[1] >= k:
                print("Yes")
            else:
                print("No")
        elif one_index == len(run_length) - 1:
            left = run_length[-2]
            if left[0] == "0":
                print("No")
            elif one_cnt + left[1] >= k:
                print("Yes")
            else:
                print("No")
        else:
            left = run_length[one_index - 1]
            right = run_length[one_index + 1]
            if left[0] == "0" and right[0] == "0":
                print("No")
            elif left[0] == "?" and right[0] == "?":
                print("Yes" if left[1] + one_cnt + right[1] == k else "No")
            elif left[0] == "?":
                print("Yes" if left[1] + one_cnt >= k else "No")
            else:
                print("Yes" if right[1] + one_cnt >= k else "No")
    else:
        # "1" の連続が 2 つ以上含まれる
        left_one_index = one_indexes[0]
        right_one_index = one_indexes[-1]

        if any(ch == "0" for ch, _ in run_length[left_one_index : right_one_index + 1]):
            print("No")
            continue

        one_cnt = sum(
            cnt for _, cnt in run_length[left_one_index : right_one_index + 1]
        )

        if one_cnt > k:
            print("No")
        elif one_cnt == k:
            print("Yes")
        elif left_one_index == 0:
            try:
                right = run_length[right_one_index + 1]
                if right[0] == "0":
                    print("No")
                elif one_cnt + right[1] >= k:
                    print("Yes")
                else:
                    print("No")
            except:
                print("No")
        elif right_one_index == len(run_length) - 1:
            try:
                left = run_length[left_one_index - 1]
                if left[0] == "0":
                    print("No")
                elif one_cnt + left[1] >= k:
                    print("Yes")
                else:
                    print("No")
            except:
                print("No")
        else:
            left = run_length[left_one_index - 1]
            right = run_length[right_one_index + 1]
            if left[0] == "0" and right[0] == "0":
                print("No")
            elif left[0] == "?" and right[0] == "?":
                print("Yes" if left[1] + one_cnt + right[1] == k else "No")
            elif left[0] == "?":
                print("Yes" if left[1] + one_cnt >= k else "No")
            else:
                print("Yes" if right[1] + one_cnt >= k else "No")
