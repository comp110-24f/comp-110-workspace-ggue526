"""Practice using a while loop to iterate over a string."""

__author__ = 730812817


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    position: int = 0
    while position < len(phrase):
        if phrase[position] == search_char:
            count += 1
        position += 1
    return count
