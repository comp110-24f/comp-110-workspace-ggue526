"""Summing the elements of a list using different loops."""

__author__ = "730812817"


def w_sum(vals: list[float]) -> float:
    # does "if !(len(vals)):" work?
    if len(vals) == 0:
        return 0.0

    sum: float = 0
    count: int = 0
    while count < len(vals):
        sum += vals[count]
        count += 1
    return sum


def f_sum(vals: list[float]) -> float:
    if len(vals) == 0:
        return 0.0

    sum: float = 0
    for i in vals:
        sum += i
    return sum


def f_range_sum(vals: list[float]) -> float:
    if len(vals) == 0:
        return 0.0

    sum: float = 0
    for i in range(len(vals)):
        sum += vals[i]
    return sum
