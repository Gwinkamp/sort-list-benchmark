from typing import List

from comparable import Comparable


def find_smallest_element(arr: List[Comparable]) -> int:
    smallest_item = arr[0]
    smallest_idx = 0

    for idx in range(1, len(arr)):
        item = arr[idx]
        if item < smallest_item:
            smallest_item = item
            smallest_idx = idx

    return smallest_idx


def selection_sort(arr: List[Comparable]) -> List[Comparable]:
    sorted_arr = []

    while len(arr) != 0:
        smallest_idx = find_smallest_element(arr)
        sorted_arr.append(arr.pop(smallest_idx))

    return sorted_arr
