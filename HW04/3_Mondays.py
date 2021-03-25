"""
3. Напишите программу, которая принимает год, и возвращает список дат всех понедельников в данном году.
   Работа с датами (можно использовать любые модули и гуглить)
"""

import sys
from datetime import datetime, timedelta

str1 = input('Input any year (format YYYY): ')
if not str1.isdigit() or len(str1) != 4:
    print(f"'{str1}' is not correct!")
    sys.exit(0)

date1 = datetime.strptime(str1, '%Y')

while date1.strftime('%Y') == str1:
    if date1.strftime('%a') == 'Mon':
        print(date1)
    date1 = date1 + timedelta(days=1)