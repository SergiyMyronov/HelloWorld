"""
1. Реализовать калькулятор, как делали на прошлом дз, но уже с обработкой ошибок (try, except)
"""

"""
2. Нужно сделать что бы код не падал, а был обработан каждый случай в отдельном except.
 На код стоит посмотреть внимательно, может что-то в нем не так)
"""
import sys

# CALCULATOR WITH TRY EXCEPT

operation: str = input('Input math operation (+, -, *, /, //, *2, **): ')

if operation in {'+', '-', '*', '/', '//', '*2', '**'}:

    first_value: str = input('Input a value: ')
    try:
        first_value = int(first_value)
    except ValueError:
        print(f"ERROR: The '{first_value}' is not a digit!")
        sys.exit(0)

    if operation == '*2':
        print(f'Result: {first_value * first_value}')
        sys.exit(0)
    else:
        second_value: str = input('Input second value: ')
        try:
            second_value = int(second_value)
        except ValueError:
            print(f"ERROR: The '{second_value}' is not a digit!")
            sys.exit(0)

        if operation == '+':
            print(f'Result: {first_value + second_value}')
        elif operation == '-':
            print(f'Result: {first_value - second_value}')
        elif operation == '*':
            print(f'Result: {first_value * second_value}')
        elif operation == '**':
            print(f'Result: {first_value ** second_value}')
        elif operation == '/':
            try:
                print(f'Result: {first_value / second_value}')
            except ZeroDivisionError:
                print('ERROR: The second value must not be zero!')
                sys.exit(0)
        elif operation == '//':
            try:
                print(f'Result: {first_value // second_value}')
            except ZeroDivisionError:
                print('ERROR: The second value must not be zero!')
else:
    print('Invalid operation')
