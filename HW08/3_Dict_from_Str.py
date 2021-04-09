
from collections import Counter

"""
3. Реализовать функцию, которая принимает строку и расделитель и возвращает словарь {слово: количество повторений} 
(частотный словарь)
"""


def converter(str1: str, sep1: str):

    dict1 = dict(Counter(str1.split(sep1)))

    return dict1

my_str = input('String ')
delimiter = input('delimiter ')

print(converter(my_str, delimiter))

