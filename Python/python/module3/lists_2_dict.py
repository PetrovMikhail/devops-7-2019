from typing import Dict, List


def lists_2_dict(first_list: List, second_list: List) -> Dict:
    if len(first_list) != len(second_list):
        raise ValueError("Lists have different lengths!")
    return dict(zip(first_list, second_list))
