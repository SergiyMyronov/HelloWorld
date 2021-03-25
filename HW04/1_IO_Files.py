"""
1. Создать файл (расширение на выбор txt, py, bin, json, yaml и тп), в нем написать текст.
 - Считать данные с файла и вывести в консоль
 - Считать данные с этого же файла и записать в новый файл
 - Считать данные с этого же файла, преобразовать (любые операции) и записать в этот же файл с разделителем
   (пробел, точка, запятая и тп)
"""

# FILE READING

import sys

try:
    file1 = open('test1.txt')
except FileNotFoundError:
    print("ERROR: File 'tets1.txt' not found!")
    sys.exit(0)

data1 = file1.read()
print(data1)
file1.close()

# FILE WRITING

file2 = open('test2.txt', mode='w')
file2.write(data1)
file2.close()

# TRANSFORMING AND WRITING DATA

file1 = open('test1.txt', mode='w')

data2 = ''

for word in data1.split():
    data2 = data2 + word + '\n'

file1.write(data2)

file1.close()
