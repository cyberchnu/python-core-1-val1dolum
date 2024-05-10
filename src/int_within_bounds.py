def int_within_bounds(number, lower_bound, upper_bound):
    if not isinstance(number, int):
        return False
    return lower_bound <= number < upper_bound
print(int_within_bounds(7, 4, 8))
print(int_within_bounds(7, 7, 7))
print(int_within_bounds(2.5, 3.5, 4.5))
