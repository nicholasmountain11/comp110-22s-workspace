"""Tests for ex06."""

__author__ = "730477365"

from exercises.ex06.dictionary import invert, favorite_color, count
import pytest


def test_invert() -> None:
    """Use case test for test."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_duplicate_keys() -> None:
    """Tests if invert gives a key error for duplicate keys."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_invert_use_case() -> None:
    """Use case test for invert."""
    assert invert({'water': 'drink'}) == {'drink': 'water'}


def test_favorite_color() -> None:
    """Use case test for favorite_color."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_favorite_color_tied() -> None:
    """Tests to see if a tie returns the color that appears in the dictionary first."""
    assert favorite_color({"Nick": "green", "Ali": "blue", "Molly": "yellow,", "Liz": "yellow", "Elle": "green"}) == "green"


def test_favorite_color_empty() -> None:
    """Tests favorite color with an empty string."""
    assert favorite_color({}) == ""


def test_favorite_color_use_case() -> None:
    """Use case test for favorite_color."""
    assert favorite_color({"Al": "purple", "Trevor": "white", "Alan": "white"}) == "white"


def test_count() -> None:
    """Use case test for count."""
    assert count(['a', 'a', 'a', 'a', 'b', 'b', 'c', 'c']) == {'a': 4, 'b': 2, 'c': 2}


def test_count_use_case() -> None:
    """Use case test for count."""
    assert count(["blue", "green", "beach", "green", "green", "beach"]) == {"blue": 1, "green": 3, "beach": 2}


def test_count_empty() -> None:
    """Tests count for an empty string."""
    assert count([]) == {}