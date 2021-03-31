"""
3. Напишите функцию is_prime, которая принимает 1 аргумент (число) и возвращает True, если число простое, иначе False
Простое число - это число, которое делится без остатка только на себя и на 1
"""

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    if num > 1:
        return True
    else:
        return False

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(f'{i} {is_prime(i)}')
