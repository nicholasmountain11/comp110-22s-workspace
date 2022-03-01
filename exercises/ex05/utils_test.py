"""Tests for utils."""

__author__ = "730477365"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens() -> None:
    """Tests a use case for only_evens."""
    assert only_evens([2, 5, 8, 6, 7]) == [2, 8, 6]


def test_only_evens_use_case() -> None:
    """Tests a use case for only_evens."""
    assert only_evens([1, 2, 3]) == [2]


def test_only_evens_none_work() -> None:
    """Tests only_evens if all the numbers in a list are odd."""
    assert only_evens([1, 3, 5]) == []


def test_only_evens_empty_list() -> None:
    """Tests only_evens with an empty list."""
    assert only_evens([]) == []


def test_sub() -> None:
    """Tests a use case for sub."""
    assert sub([4, 8, 0, 3, 9, 32], 2, 5) == [0, 3, 9]


def test_sub_use_case() -> None:
    """Tests a use case for sub."""
    assert sub([10, 20, 30, 40, 50], 1, 4) == [20, 30, 40]


def test_sub_negative_start() -> None:
    """Tests sub with a negative starting index."""
    assert sub([10, 20, 30, 40, 50], -1, 4) == [10, 20, 30, 40]


def test_sub_end_too_high() -> None:
    """Tests sub for when the end index > len of the given list."""
    assert sub([10, 20, 30, 40, 50], 1, 9) == [20, 30, 40, 50]


def test_sub_len_zero() -> None:
    """Tests sub for an empty list."""
    assert sub([], 1, 4) == []


def test_sub_start_above_len() -> None:
    """Tests sub for when the starting value is greater than len of the given list."""
    assert sub([10, 20, 30], 7, 10) == []


def test_sub_end_zero() -> None:
    """Tests sub for when the end value is <= 0."""
    assert sub([10, 20, 30], -3, 0) == []


def test_concat() -> None:
    """Tests a use case for concat."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_concat_empty_list() -> None:
    """Tests concat for an empty list."""
    assert concat([], []) == []


def test_concat_two() -> None:
    """Tests a use case for concat."""
    assert concat([3, 4, 7, 9], [2, 4, 3]) == [3, 4, 7, 9, 2, 4, 3]