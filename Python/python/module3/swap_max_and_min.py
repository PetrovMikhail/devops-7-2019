from typing import List


def swap_max_and_min(values_list: List) -> List:
    if len(values_list) != len(set(values_list)):
        raise ValueError("Elements in list are not unique!")
    reverse_list = list(values_list)
    for value in values_list:
        if not isinstance(value, int):
            raise TypeError("List include element with wrong type!")
        if value == max(values_list):
            max_index = values_list.index(value)
        if value == min(values_list):
            min_index = values_list.index(value)
    reverse_list[max_index] = min(values_list)
    reverse_list[min_index] = max(values_list)
    return reverse_list
