"""
2. Преобразовать дату. Нужно написать код, который из Feb 12 2019 2:41PM сделает 2019-02-12 14:41:00
"""

from datetime import datetime

str1 = 'Feb 12 2019 2:41PM'
date1 = datetime.strptime(str1, '%b %d %Y %I:%M%p')

# Source string
print(f'Source string: {str1}')

# Local datetime format
print(f"Local datetime format: {date1.strftime('%c')}")

# Target format
print(f"Target format: {date1.strftime('%Y-%m-%d %H:%M:%S')}")

