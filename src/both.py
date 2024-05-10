def both(number1, number2):
    return (number1 < 0 and number2 < 0) or (number1 > 0 and number2 > 0) or (number1 == 0 and number2 == 0)
print(both(2, -2))
print(both(25, 25))
print(both(0, 0))
print(both(-77, 42))
