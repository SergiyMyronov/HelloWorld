"""
3. Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.
"""

from collections import Counter

text1 = input('Введите текст: ')

if text1:
    Common1 = Counter(text1.split()).most_common(1)
    Longest1 = sorted(text1.split(), key=len)
    print(f'The most common word is "{Common1[0][0]}"')
    print(f'The longest word is "{Longest1[-1]}"')
else:
    print('You have not entered any word!')