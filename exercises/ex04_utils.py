"""Messing with lists."""

__author__ = "730812817"


# Checks if all elements of num_list are num
def all(num_list: list[int], num: int) -> bool:
    count: int = 0
    while count < len(num_list):
        if num_list[count] != num:
            return False
        count += 1
    return True


# Finds the max of a given list
def max(num_list: list[int]) -> int:
    # in case of empty lsit
    if len(num_list) == 0:
        raise ValueError("max() arg is an empty List")

    count: int = 0
    biggest_num: int = 0
    while count < len(num_list):
        # checks each index against biggest_num
        if num_list[count] > biggest_num:
            biggest_num = num_list[count]
        count += 1
    return biggest_num


# Checks if num_list1 is equal to num_list2
def is_equal(num_list1: list[int], num_list2: list[int]) -> bool:
    # in case of differing length
    if len(num_list1) != len(num_list2):
        return False
    count: int = 0
    while count < len(num_list1):
        if num_list1[count] != num_list2[count]:
            return False
        count += 1
    return True


# appends all elements of num_list2 to num_list1
def extend(num_list1: list[int], num_list2: list[int]) -> None:
    count = 0
    while count < len(num_list2):
        num_list1.append(num_list2[count])
        count += 1
