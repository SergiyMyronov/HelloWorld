"""
1. У вас есть массив чисел, составьте из них максимальное число. Например:
 [61, 228, 9] -> 961228
"""


def max_num(list1: list):

    list1.sort(key=str, reverse=True)

    s_result = ''
    for s in list1:
        s_result += str(s)

    return int(s_result)


l1 = [61, 228, 9]

print(max_num(l1))



