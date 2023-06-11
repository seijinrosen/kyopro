S = input()


def solve() -> bool:
    if S == "AKIHABARA":
        return True

    if S in {
        "KIHABARA",
        "AKIHBARA",
        "AKIHABRA",
        "AKIHABAR",
    }:
        return True

    if S in {
        "KIHBARA",
        "KIHABRA",
        "KIHABAR",
        "AKIHBRA",
        "AKIHBAR",
        "AKIHABR",
    }:
        return True

    if S in {
        "KIHBRA",
        "KIHBAR",
        "KIHABR",
        "AKIHBR",
    }:
        return True

    if S == "KIHBR":
        return True

    return False


print("YES" if solve() else "NO")
