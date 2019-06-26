def multiple_in_range(min_value: int, max_value: int):
    return [x for x in range(min_value, max_value + 1) if (x % 7 == 0 and x % 5 != 0)]
