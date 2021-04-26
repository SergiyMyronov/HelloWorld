"""
Создать класс воина, создать 2 или больше объектов воина с соответствующими воину атрибутами. Реализовать методы,
которые позволять добавить здоровья, сменить оружие. Реализовать возможность драки 2х воинов с потерей здоровья,
приобретения опыта.
Следует учесть:
 - у воина может быть броня
 - здоровье не может быть меньше 0
 - броня не может быть меньше 0
 - здоровье не тратится пока броня не 0
Было бы неплохо добавить возможность воину носить несколько видов оружия и при сломаном текущем заменить его (опционально)
"""
from random import randint, choice


class Weapon:
    def __init__(self, name, power):
        self.name = name
        self.power = power


class Warrior:
    def __init__(self, weapon: Weapon, name: str, health: int):
        self.weapon = weapon
        self.name = name
        self.health = health
        self.armor = 0
        self.experience = 0
        self.status = 'alive'

    def add_health(self, value):
        if self.status == 'dead':
            print(f"{self.name} is dead! Sorry, we can't change it!")
            return
        self.health += value
        if self.health < 0:
            self.health = 0
            self.status = 'dead'
            print(f'{self.name} is dead!')

    def add_experience(self, value):
        self.experience += value
        self.add_weapon_power()

    def add_weapon_power(self):
        # увеличиваем мощность оружия пропорционально опыту воина
        if self.experience > 9:
            self.weapon.power = round(self.weapon.power * 1.6)
        elif self.experience > 6:
            self.weapon.power = round(self.weapon.power * 1.4)
        elif self.experience > 3:
            self.weapon.power = round(self.weapon.power * 1.2)

    def change_weapon(self, weapon):
        self.weapon = weapon
        self.add_weapon_power()

    def add_armor(self, value):
        if self.status == 'dead':
            print(f"{self.name} is dead! Sorry, we can't change it!")
            return
        self.armor += value
        if self.armor < 0:
            self.add_health(self.armor)
            self.armor = 0

    def hit_another(self, another_warrior):
        if self.status == 'dead':
            print(f"{self.name} is dead! He can't hit anybody!")
            return
        if another_warrior.status == 'dead':
            print(f"{another_warrior.name} is already dead! Don't hit him!")
            return
        if another_warrior.armor:
            another_warrior.add_armor(-self.weapon.power)
        else:
            another_warrior.add_health(-self.weapon.power)
        if another_warrior.status == 'dead':
            print(f'!!!!! {self.name} won !!!!!')
            if another_warrior.experience:
                self.add_experience(another_warrior.experience)
            else:
                self.add_experience(1)
            if another_warrior.weapon.power > self.weapon.power:
                self.change_weapon(another_warrior.weapon)
                print(f'{self.name} got {self.weapon.name}!')


def random_choose_weapon():
    weapon_list = []
    for i in range(50):
        weapon_list.append(Weapon(
            name='Weapon-' + str(i),
            power=randint(5, 50)
        ))
    return choice(weapon_list)


def main_fighting_area():
    warrior1 = Warrior(name='Oleg', health=randint(80, 200), weapon=random_choose_weapon())
    warrior1.add_armor(randint(1, 40))
    warrior1.add_experience(randint(0, 10))
    warrior2 = Warrior(name='Vasyl', health=randint(80, 200), weapon=random_choose_weapon())
    warrior2.add_armor(randint(10, 40))
    warrior2.add_experience(randint(0, 10))

    counter = 1
    print(f'\nInitial status:')
    print(f'{warrior1.name} H={warrior1.health} A={warrior1.armor} E={warrior1.experience} WP={warrior1.weapon.power}\t\t'
          f'{warrior2.name} H={warrior2.health} A={warrior2.armor} E={warrior2.experience} WP={warrior2.weapon.power}\n')
    while warrior1.status == 'alive' and warrior2.status == 'alive':
        print(f'Round {counter}')
        warrior1.hit_another(warrior2)
        warrior2.hit_another(warrior1)
        print(f'{warrior1.name} H={warrior1.health} A={warrior1.armor} E={warrior1.experience} WP={warrior1.weapon.power}\t\t'
              f'{warrior2.name} H={warrior2.health} A={warrior2.armor} E={warrior2.experience} WP={warrior2.weapon.power}\n')
        counter += 1


main_fighting_area()
