"""
1. Разминочная задача на ввод/вывод.
    Написать программу, которая запросит у
    пользователя что-то, а потом выведет
    результат в консоль.
"""

#import sys

# I/O operations

name = input('What is your name: ')
if len(name) > 0:
    print(f'Hi {name}, your name consists of {len(name)} symbols!')
else:
    print("You didn't enter any symbol!")


