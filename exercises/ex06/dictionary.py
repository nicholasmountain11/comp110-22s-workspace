"""Docstring."""

__author__ = "730477365"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a given dictionary."""
    new_x: dict[str, str] = dict()
    for i in x:
        if x[i] in new_x:
            raise KeyError("Cannot have duplicate keys.")
        new_x[x[i]] = i
    return new_x


def favorite_color(x: dict[str, str]) -> str:
    """Finds the most common favorite color in a dictionary of favorite colors."""
    x_new: dict[str, int] = dict()
    for i in x:
        if x[i] in x_new:
            x_new[x[i]] += 1
        else:
            x_new[x[i]] = 1
    highest_value: int = 0
    highest_key: str = ""
    for i in x_new:
        if x_new[i] > highest_value:
            highest_value = x_new[i]
            highest_key = i
    return highest_key


def count(x: list[str]) -> dict[str, int]:
    """Counts the number of times an item appears in a list."""
    x_dict: dict[str, int] = dict()
    for i in x:
        if i in x_dict:
            x_dict[i] += 1
        else:
            x_dict[i] = 1
    return x_dict