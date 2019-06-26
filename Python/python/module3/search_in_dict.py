from typing import Set, Dict


def search_in_dict(user_set: Set, big_dict: Dict) -> Set:
    result_set = set(list())
    for el in user_set:
        if el in big_dict.keys():
            result_set.update({el})
    return result_set
