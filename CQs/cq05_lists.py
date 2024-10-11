"""Mutating functions."""

__author__ = "730812817"


def manual_append(the_list: list[int], num: int) -> None:
    the_list.append(num)


def double(the_list: list[int]) -> None:
    count: int = 0
    while count < len(the_list):
        the_list[count] *= 2
        count += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
