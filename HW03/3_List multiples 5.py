
"""
4. Создать список, где все элементы будут кратные 5ти (упражнение на функцию range)
"""

"""
5. Вывести в консоль (функция print) максимальное и минимальное значение из списка в задании 4 и сумму всех елементов 
этого списка
"""

# RANGE

# First way
List5 = []
for i in range(1,11):
    List5.append(i*5)

print(List5)

# Second way
List5 = []
for i in range(5, 55, 5):
    List5.append(i)

print(List5)


# MAX, MIN, SUM OF LIST5

print(f'\nMax is {max(List5)}, \nMin is {min(List5)}, \nSum is {sum(List5)}')

