"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, last, linkify, scale, value_at, max

__author__ = "730477365"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise an value error."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return a reference to its last Node."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_last_one_node() -> None:
    """Last of a one Node list should return reference to its one value."""
    one_value_list = Node(1, None)
    assert last(one_value_list) == 1


def test_value_at_empty() -> None:
    """value_at of an empty list should raise an index error."""
    with pytest.raises(IndexError):
        value_at(None, 0)


def test_value_at_zero_index() -> None:
    """When index is 0, should return the index of the current Node."""
    assert value_at(Node(10, Node(20, Node(30, None))), 0) == 10


def test_value_at() -> None:
    """value_at should return the data for a given Node at a given index."""
    assert value_at(Node(10, Node(20, Node(30, None))), 1) == 20


def test_value_at_use_case() -> None:
    """value_at should return the data for a given Node at a given index."""
    assert value_at(Node(10, Node(20, Node(30, None))), 2) == 30


def test_value_at_index_too_high() -> None:
    """When index is out of range of the list, should raise Index error."""
    with pytest.raises(IndexError):
        value_at(Node(10, Node(20, Node(30, None))), 3) 


def test_max_none() -> None:
    """Should raise ValueError if max is called with None."""
    with pytest.raises(ValueError):
        max(None)


def test_max() -> None:
    """Should return the maximum data value of the given linked list."""
    assert max(Node(10, Node(20, Node(30, None)))) == 30


def test_max_use_case_two() -> None:
    """Should return the maximum data value of the given linked list."""
    assert max(Node(10, Node(30, Node(20, None)))) == 30


def test_max_use_case_three() -> None:
    """Should return the maximum data value of the given linked list."""    
    assert max(Node(30, Node(20, Node(10, None)))) == 30


def test_linkify() -> None:
    """Should return a linked list of Nodes with same values and order as a given list."""
    assert str(linkify([1, 2, 3])) == "1 -> 2 -> 3 -> None"


def test_linkify_empty_list() -> None:
    """Should return None if given an empty list."""
    assert str(linkify([])) == "None"


def test_scale() -> None:
    """Should return a new linked list where each value is multiplied by a given factor."""
    assert str(scale(linkify([1, 2, 3]), 2)) == "2 -> 4 -> 6 -> None"


def test_scale_empty() -> None:
    """An input of an empty Node should return None."""
    assert str(scale(linkify([]), 2)) == "None"