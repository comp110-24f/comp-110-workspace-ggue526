"""Coordinates."""

__author__ = "730812817"


def get_coords(xs: str, ys: str) -> None:
    count1: int = 0
    count2: int = 0
    # im imagining fpr loops here so i can be happy
    while count1 < len(xs):
        while count2 < len(ys):
            print("(" + xs[count1] + "," + ys[count2] + ")")
            count2 += 1
        count1 += 1
        count2 = 0
