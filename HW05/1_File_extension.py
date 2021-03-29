"""
1. Напишите программу, которая принимает имя файла и выводит его расширение.
    Если расширение у файла определить невозможно, выбросите исключение.
"""

file_name = input('Введите имя файла: ')
if file_name == '' or file_name[0] == '.' or '.' not in file_name or file_name[-1] == '.':
    raise RuntimeError('Incorrect file extension')
else:
    print(f"File '{file_name}' has extension '{file_name[file_name.index('.')+1::]}'")
