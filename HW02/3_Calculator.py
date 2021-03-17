
"""
3. Дописать калькулятор, добавив операции умножения, деления, целочисленного деления и возведения в квадрат. 
    Обязательно программа должна обрабатывать тонкие места и не падать
"""


# CALCULATOR

while 1:
    operation: str = input('Input math operation (+, -, *, /, //, *2, **): ')

    if operation in {'+', '-', '*', '/', '//', '*2', '**'}:

        first_value: str = input('Input a value: ')
        if not first_value.isdigit():
            print(f"'{first_value}' is not a digit. Try again!")
            continue
        first_value: int = int(first_value)

        if operation == '*2':
            print(f'Result: {first_value * first_value}')
            break
        else:
            second_value: str = input('Input second value: ')
            if not second_value.isdigit():
                print(f"'{second_value}' is not a digit. Try again!")
                continue
            second_value: int = int(second_value)

            if operation == '+':
                print(f'Result: {first_value + second_value}')
            elif operation == '-':
                print(f'Result: {first_value - second_value}')
            elif operation == '*':
                print(f'Result: {first_value * second_value}')
            elif operation == '/':
                print(f'Result: {first_value / second_value}')
            elif operation == '//':
                print(f'Result: {first_value // second_value}')
            elif operation == '**':
                print(f'Result: {first_value ** second_value}')
            break
    else:
        print('Invalid operation. Try again!')
