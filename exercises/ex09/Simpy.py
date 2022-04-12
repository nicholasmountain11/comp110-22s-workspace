"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730477365"


class Simpy:
    """Utility class for numerical operations."""
    values: list[float]

    def __init__(self, values):
        """Initializes values attribute."""
        self.values = values

    def __str__(self) -> str:
        """String representation of the values attribute."""
        return f"Simpy({self.values})"

    def fill(self, value: float, value_amount: int) -> None:
        """Fills a Simpy's values with a specific number of repeating values."""
        self.values = []
        i: int = 0
        while i < value_amount:
            self.values.append(value)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values attrictue with a range of values."""
        assert step != 0.0
        current_number: float = start
        while current_number != stop:
            self.values.append(current_number)
            current_number += step 

    def sum(self) -> float:
        """Compute and return the sum of all items in the values attribute."""
        return sum(self.values)

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Overloads addition operator."""
        result = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        else:
            for value in self.values:
                result.values.append(value + rhs)
        return result

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Overloads power operator."""
        result = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        else:
            for value in self.values:
                result.values.append(value ** rhs)
        return result

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Overloads == operator."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] == rhs.values[i])
                i += 1
        else:
            for value in self.values:
                result.append(value == rhs)  
        return result

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Overloads == operator."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] > rhs.values[i])
                i += 1
        else:
            for value in self.values:
                result.append(value > rhs)  
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overloads subsription operator."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            result = Simpy([])
            i: int = 0
            while i < len(rhs):
                if rhs[i]:
                    result.values.append(self.values[i])
                i += 1
            return result