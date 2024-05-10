def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)
print(fizz_buzz(27))
print(fizz_buzz(25))
print(fizz_buzz(120))
print(fizz_buzz(26))
