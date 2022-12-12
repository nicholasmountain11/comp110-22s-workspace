

def reverse_multiply(x: list[int]) -> list[int]:
    result: list[int] = []
    i: int = 0
    while i < len(x):
        result.append(x[0 - i] * 2)
        i += 1
    return result


def multiples(x: list[int]) -> list[bool]:
    result: list[bool] = []
    i: int = 0
    while i < len(x):
        if x[i] % x[i - 1] == 0:
            result.append(True)
        else:
            result.append(False)
        i += 1
    return result


def merge_lists(x: list[str], y: list[int]) -> dict[str, int]:
    result: dict[str, int] = {}
    if len(x) != len(y):
        return result
    else:
        i: int = 0
        while i < len(x):
            result[x[i]] = y[i]
            i += 1
    return result


print(merge_lists(["blue", "yellow", "red"], [5, 2, 4]))