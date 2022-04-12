from __future__ import annotations

from typing import Union


class StrArray:
    items: list[str]

    def __init__(self, items):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        """Add is a vectorized operation that applies to all items.

        When rhs is a str, it is concatenated to every item in a new StrArray
        """
        result: list[str] = []
        # Establish a result list of strings that is empty
        # Loop through every item in self.items
        # Append the concatenation of item with rhs to your result list
        # After loop, return a new StrArray object concatenated with result list
        if isinstance(rhs, str):
            for item in self.items:
                result.append(item + rhs)
        else:
            for i in range(0, len(self.items)):
                result.append(self.items[i] + rhs.items[i])
        return StrArray(result)


first: StrArray = StrArray(["Armando", "Brady", "Caleb"])
last: StrArray = StrArray(["Bacot", "Manek", "Love"])
print(first + "!")
print(first + last)
print(last + ", " + first)