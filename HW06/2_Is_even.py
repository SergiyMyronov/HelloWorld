"""
2. Написать функцию, которая вернет True если число четное и False если не четное
"""

def is_even(num):
    return num % 2 == 0

for i in [1, 2, 3, 3, 3, 4, 5, 6, 6, 6, 6, 7, 8, 9]:
    print(is_even(i))
