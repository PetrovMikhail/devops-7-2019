from typing import Dict


def dict_swap(initial_dict: Dict) -> Dict:
    result_dict = dict()
    for key, value in initial_dict.items():
        result_dict.update({value: key})
    return result_dict
