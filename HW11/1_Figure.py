"""
1.Реализовать класс фигуры. На основе фигуры реализовать класс треугольника, квадрата и прямоугольника с
методами подсчета площади и периметра. Методы должны возвращать (return) значение, а не принтить (это важно)
"""


class Polygon:
    def __init__(self, name):
        self.name = name


class Triangle(Polygon):
    def __init__(self, name, side1, side2, side3):
        super().__init__(name)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @property
    def perimeter(self):
        try:
            p = self.side1 + self.side2 + self.side3
        except:
            raise TypeError('Стороны треугольника должны быть целыми числами')
        return p

    @property
    def area(self):
        p = self.perimeter / 2
        a = (p * (p-self.side1) * (p-self.side2) * (p-self.side3)) ** (0.5)
        return a


class Rectangle(Polygon):
    def __init__(self, name, side1, side2):
        super().__init__(name)
        self.side1 = side1
        self.side2 = side2

    @property
    def perimeter(self):
        try:
            p = (self.side1 + self.side2) * 2
        except:
            raise TypeError('Стороны прямоугольника должны быть целыми числами')
        return p

    @property
    def area(self):
        try:
            a = self.side1 * self.side2
        except:
            raise TypeError('Стороны прямоугольника должны быть целыми числами')
        return a


class Square(Polygon):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    @property
    def perimeter(self):
        try:
            p = self.side * 4
        except:
            raise TypeError('Сторона квадрата должна быть целым числом')
        return p

    @property
    def area(self):
        try:
            a = self.side ** 2
        except:
            raise TypeError('Сторона квадрата должна быть целым числом')
        return a


def main():
    p_type = input('Выберите фигуру (t - треугольник, r - прямоугольник, s - квадрат): ')
    if p_type == 't':
        try:
            s1 = int(input('Введите длину первой стороны: '))
            s2 = int(input('Введите длину второй стороны: '))
            s3 = int(input('Введите длину третьей стороны: '))
        except:
            raise TypeError('Стороны треугольника должны быть целыми числами')
        polyg = Triangle('Треугольник', s1, s2, s3)
    elif p_type == 'r':
        try:
            s1 = int(input('Введите длину первой стороны: '))
            s2 = int(input('Введите длину второй стороны: '))
        except:
            raise TypeError('Стороны прямоугольника должны быть целыми числами')
        polyg = Rectangle('Прямоугольник', s1, s2)
    elif p_type == 's':
        try:
            s1 = int(input('Введите длину стороны: '))
        except:
            raise TypeError('Сторона квадрата должна быть целым числом')
        polyg = Square('Квадрат', s1)
    else:
        raise Exception('Некорректный тип фигуры!')

    print(f'Периметр {polyg.name}а = {polyg.perimeter}\nПлощадь {polyg.name}а = {polyg.area}')


if __name__ == '__main__':
    main()