def squares_sum(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i * i
    return total_sum
print(squares_sum(25))
print(squares_sum(42))
print(squares_sum(8))
