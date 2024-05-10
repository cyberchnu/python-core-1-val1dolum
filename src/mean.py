def mean(number):
    num_str = str(number)
    digit_sum = sum(int(digit) for digit in num_str)
    mean_value = digit_sum // len(num_str)
    return mean_value
print(mean(25))
print(mean(23102004))
print(mean(777))
