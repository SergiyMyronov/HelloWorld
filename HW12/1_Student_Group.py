"""
 Создать класс, описывающий группу студентов - `Group`. Данный класс хранит студентов в виде уникального набора объектов
 `Student` также реализованного в виде соответствующего класса.
В классах реализовать необходимай набор атрибутов (Например класс `Student` должен иметь атрибуты `name`, `age`,
`grades` и тп), а так же необходимый набор методов экземпляра для работы с этими объектами.
    Реализовать функционал, который позволит:
     1. Покинуть студенту группу
     2. Перевестись в другую группу
     3. Покзать средний балл отдельного студента
     4. Показать средний балл по группе
     (по желанию и возможностям можно еще добавить функционала)
"""


from uuid import uuid4


class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.__grades = {'Algebra': 0, 'Geometry': 0, 'Statistics': 0, 'Physics': 0, 'Economics': 0}

    @property
    def calc_avg_grade(self):
        return float(sum([self.__grades[key] for key in self.__grades]) / len(self.__grades))

    def set_grade(self, subject, grade):
        try:
            self.__grades[subject] = grade
        except:
            raise Exception(f'Incorrect subject {subject}')


class Group:
    def __init__(self, group_number):
        self.group_number = group_number
        self.__students = {}

    @property
    def str_student_list(self):
        st_list = []
        for item in self.__students:
            st_list.append(self.__students[item].name + ' ' + str(self.__students[item].age))
        return st_list

    @property
    def student_dict(self):
        return self.__students

    def add_student(self, student):
        self.__students.setdefault(student.student_id, student)

    def remove_student(self, student):
        try:
            del self.__students[student.student_id]
        except:
            raise Exception(f'There is no student {student.name} {student.age} {student.student_id} in the group {self.group_number}')

    def transfer_student(self, student, new_group):
        try:
            del self.__students[student.student_id]
        except:
            raise Exception(
                f'There is no student {student.name} {student.age} {student.student_id} in the group {self.group_number}')
        new_group.add_student(student)

    @property
    def calc_group_avg_grade(self):
        avg = 0
        try:
            avg = float(sum([self.__students[key].calc_avg_grade for key in self.__students]) / len(self.__students))
        finally:
            return avg


def main():
    gr1 = Group('1')
    gr2 = Group('2')

    st1 = Student(uuid4(), 'Иванов', 20)
    st2 = Student(uuid4(), 'Петров', 22)
    st3 = Student(uuid4(), 'Сидоров', 18)

    st1.set_grade('Algebra', 95)
    st1.set_grade('Geometry', 80)
    st1.set_grade('Statistics', 90)
    st1.set_grade('Physics', 65)
    st1.set_grade('Economics', 88)

    st2.set_grade('Algebra', 65)
    st2.set_grade('Geometry',55)
    st2.set_grade('Statistics', 58)
    st2.set_grade('Physics', 76)
    st2.set_grade('Economics', 45)

    st3.set_grade('Algebra', 78)
    st3.set_grade('Geometry', 72)
    st3.set_grade('Statistics', 68)
    st3.set_grade('Physics', 95)
    st3.set_grade('Economics', 82)

    gr1.add_student(st1)
    gr1.add_student(st2)
    gr2.add_student(st3)

    print(f"\nStudent's Avg:\n{st1.name} {st1.calc_avg_grade}, "
          f"{st2.name} {st2.calc_avg_grade}, {st3.name} {st3.calc_avg_grade}\n")

    print(f'Students of the Group{gr1.group_number}: {gr1.str_student_list}')
    print(f'Avg grade of Group{gr1.group_number}: {gr1.calc_group_avg_grade}\n')

    print(f'Students of the Group{gr2.group_number}: {gr2.str_student_list}')
    print(f'Avg grade of Group{gr2.group_number}: {gr2.calc_group_avg_grade}\n')

    gr1.transfer_student(st2, gr2)
    print('************* TRANSFER **************\n')

    print(f'Students of the Group{gr1.group_number}: {gr1.str_student_list}')
    print(f'Avg grade of Group{gr1.group_number}: {gr1.calc_group_avg_grade}\n')

    print(f'Students of the Group{gr2.group_number}: {gr2.str_student_list}')
    print(f'Avg grade of Group{gr2.group_number}: {gr2.calc_group_avg_grade}\n')

    gr2.remove_student(st3)
    print('************* REMOVE **************\n')

    print(f'Students of the Group{gr1.group_number}: {gr1.str_student_list}')
    print(f'Avg grade of Group{gr1.group_number}: {gr1.calc_group_avg_grade}\n')

    print(f'Students of the Group{gr2.group_number}: {gr2.str_student_list}')
    print(f'Avg grade of Group{gr2.group_number}: {gr2.calc_group_avg_grade}\n')


if __name__ == '__main__':
    main()
