"""
Описать сказку про Колобка (не обязательно про колобка) классами.
Ссылка на текст сказки  - https://nukadeti.ru/skazki/kolobok
Нужно создать классы деда, бабки, колобка, лисы (по желанию можно добавить героев) с методами, которые будут имитировать
реплики героев в сказке. Описывать реплики можно не полностью, вызывать методы нужно в очередности сченария,
как использовать - дело фонтазии))
к примеру:
class Fox(ParentClass):
    def eat_kolobok(self, kolobok):
        print('MMMM yammy') реплика лисы
        kolobok.die() метод, который описывает смерть колобка
fox = Fox()
fox.eat_kolobok(kolobok)
Тут описан пример как можно вызвать метод колобка в методе лисы, т.е. действие обязательно вызовет измение другого
объекта. Не стоит забывать что в питоне все типы подобны и мы можем передавать параметрами в метод/функцию любой
питоновский объект
"""


class Hero:  # базовый класс для героев
    def __init__(self, name):
        self.name = name


class Animal(Hero):  # класс зверей
    @staticmethod
    def say_wanna_eat():
        print('— Колобок, колобок! Я тебя съем.')


class Fox(Animal):  # класс хитрая лиса
    @staticmethod
    def say_sing_more():
        print('— Какая славная песенка!\n— Но ведь я, колобок, стара стала, плохо слышу; сядь-ка на мой носик да пропой еще разок погромче.',
              '\nКолобок вскочил лисе на носик и запел ту же песню.')

    @staticmethod
    def eat_kolobok(kolobok):
        print('— Спасибо, колобок! Славная песенка, еще бы послушала!\nКолобок заулыбался, а лиса — ам его! И съела колобка…')
        kolobok.die()


class Kolobok(Hero):  # класс Колобок
    @staticmethod
    def say_dont_eat_me(animal):
        print(f'— Не ешь меня, {animal.name}! Я тебе песенку спою!')

    @staticmethod
    def sing_a_song(animal):
        print(f'Я Колобок, Колобок!\nЯ по коробу скребен,\nПо сусеку метен,\nНа сметане мешон,\nДа в масле пряжон,',
              f'\nНа окошке стужон;\nЯ от дедушки ушел,\nЯ от бабушки ушел,\nИ от тебя, {animal.name}, не хитро уйти!\n')

    @staticmethod
    def die():
        print(f'\nВот и сказочке конец, а кто слушал, молодец!')


def tale():

    kolobok1 = Kolobok('Колобок')

    fox = Fox('Лиса')

    animal_list = [Animal('Заяц'), Animal('Волк'), Animal('Медведь'), fox]

    for anim in animal_list:
        print(f'Катится колобок по дороге, а навстречу ему {anim.name}:')
        anim.say_wanna_eat()
        kolobok1.say_dont_eat_me(anim)
        kolobok1.sing_a_song(anim)

    fox.say_sing_more()
    kolobok1.sing_a_song(fox)
    fox.eat_kolobok(kolobok1)


tale()
