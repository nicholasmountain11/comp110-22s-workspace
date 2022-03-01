"""Functions that in a given list create a new list with only the even numbers, only the numbers in a given range, and add the lists together."""

__author__ = "730477365"


def only_evens(numbers: list[int]) -> list[int]:
    """Returns a list with only the even numbers of a given list."""
    new_list: list[int] = list()
    for i in numbers:
        if i % 2 == 0:
            new_list.append(i)
    return new_list


def sub(numbers: list[int], start, end) -> list[int]:
    """Returns a list with only the numbers in a certain range of a given list."""
    new_list: list[int] = list()
    i: int = start
    if start < 0:
        i: int = 0
    if end > len(numbers):
        end = len(numbers)
    while start <= i < end:
        new_list.append(numbers[i])
        i += 1
    return new_list


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Returns a list that is the combination of two given lists."""
    new_list: list[int] = list()
    for i in list_1:
        new_list.append(i)
    for alt_i in list_2:
        new_list.append(alt_i)
    return new_list
