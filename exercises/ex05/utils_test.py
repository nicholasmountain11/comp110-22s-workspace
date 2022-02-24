"""Docstring."""

__author__ = "730477365"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens() -> None:
    assert only_evens([2, 5, 8, 6, 7]) == [2, 8, 6]


def test_only_evens_use_case() -> None:
    assert only_evens([1, 2, 3]) == [2]


def test_only_evens_none_work() -> None:
    assert only_evens([1, 3, 5]) == []


def test_only_evens_empty_list() -> None:
    assert only_evens([]) == []


def test_sub() -> None:
    assert sub([4, 8, 0, 3, 9, 32], 2, 5) == [0, 3, 9]


def test_sub_use_case() -> None:
    assert sub([10, 20, 30, 40, 50], 1, 4) == [20, 30, 40]


def test_sub_negative_start() -> None:
    assert sub([10, 20, 30, 40, 50], -1, 4) == [10, 20, 30, 40]


def test_sub_end_too_high() -> None:
    assert sub([10, 20, 30, 40, 50], 1, 9) == [20, 30, 40, 50]


def test_sub_len_zero() -> None:
    assert sub([], 1, 4) == []


def test_sub_start_above_len() -> None:
    assert sub([10, 20, 30], 7, 10) == []


def test_sub_end_zero() -> None:
    assert sub([10, 20, 30], -3, 0) == []


def test_concat() -> None:
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_concat_empty_list() -> None:
    assert concat([], []) == []


def test_concat_two() -> None:
    assert concat([3, 4, 7, 9], [2, 4, 3]) == [3, 4, 7, 9, 2, 4, 3]