"""Dictionary related utility functions."""

__author__ = "730477365"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV rather than just strings.
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done to free its resources
    file_handle.close()

    return result 


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in table:
        values: list[str] = []
        i: int = 0
        while i < rows and i < len(table[column]):
            values.append(table[column][i])
            i += 1
        result[column] = values
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in names:
        result[column] = table[column]
    return result


def concat(x: dict[str, list[str]], y: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in x:
        result[column] = x[column]
    for column in y:
        if column in result:
            result[column] += y[column]
        else:
            result[column] = y[column]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Count the frequency of each value in a list."""
    result: dict[str, int] = {}
    for i in values:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result


def average(first_column: list[str], second_column: list[str]) -> dict[str, float]:
    totals: dict[str, int] = {}
    i: int = 0
    while i < len(first_column):
        if first_column[i] in totals:
            totals[first_column[i]] += int(second_column[i])
        else:
            totals[first_column[i]] = int(second_column[i])
        i += 1
    result: dict[str, float] = {}
    counts: dict[str, int] = count(first_column)
    for column in totals:
        result[column] = totals[column] / counts[column]
    return result