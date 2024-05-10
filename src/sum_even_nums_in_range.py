def sum_even_nums_in_range(start, stop):
    sum_even = 0
    for num in range(start, stop + 1):
        if num % 2 == 0:
            sum_even += num
    return sum_even
print(sum_even_nums_in_range(79, 42))
print(sum_even_nums_in_range(25, 125))
print(sum_even_nums_in_range(40, 70))
