"""
2.Реализовать класс Person, у которого должно быть два атрибута: age и name. 
Также у него должен быть следующий набор методов:
    1.def know(self, another_person_object)
    который позволяет добавить другого человека в список знакомых (лист __friends (обязательно приватный атрибут)).
    2.def is_known(self, another_person_object)
    который возвращает знакомы ли два человека (True/False)
    
"""


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__friends = []

    def get_friends(self):
        return self.__friends

    def know(self, another_person):
        if isinstance(another_person, Person):
            self.__friends.append(another_person)
        else:
            raise TypeError

    def is_known(self, another_person):
        if isinstance(another_person, Person):
            found = False
            for item in self.__friends:
                if item.name == another_person.name and item.age == another_person.age:
                    found = True
            return found
        else:
            raise TypeError


def main():
    me = Person('Я', 18)

    while True:
        act = input('Введите действие("a"-добавить знакомого, "c"-проверить наличие знакомого, любой символ - выход): ')
        if act == 'a':
            name = input('Введите имя знакомого: ')
            try:
                age = int(input('Введите возраст знакомого: '))
            except:
                raise TypeError('Возраст д.б. целым числом')
            pers = Person(name, age)
            me.know(pers)
            print(f'{name}, {age} добавлен в список знакомых\n')
        elif act == 'c':
            name = input('Введите имя знакомого: ')
            try:
                age = int(input('Введите возраст знакомого: '))
            except:
                raise TypeError('Возраст д.б. целым числом')
            pers = Person(name, age)
            if me.is_known(pers):
                print(f'{name} {age} мне знаком\n')
            else:
                print(f'{name} {age} НЕТ в списке знакомых!\n')
        else:
            friends = me.get_friends()
            print('Список знакомых:')
            for item in friends:
                print(f'{item.name}, {item.age}')
            break


if __name__ == '__main__':
    main()
