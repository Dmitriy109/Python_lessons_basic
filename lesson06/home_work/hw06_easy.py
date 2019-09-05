# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
from math import sqrt

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def distance(self):
        self.AB = round(sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2))
        self.BC = round(sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2))
        self.AC = round(sqrt((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2))
        return f'Длинна AB - {round(self.AB)}\nДлинна BC - {round(self.BC)}\nДлинна AC - {round(self.AC)}\n'

    def perimeter(self):
        """Вычисляем периметр"""
        self.distance()
        self.p = self.AB + self.BC + self.AC
        return f'Периметр треугольника - {round(self.p)}'

    def area(self):
        """Вычисляем площадь"""
        self.distance()
        self.perimeter()
        self.s = sqrt(self.p/2 * (self.p/2 - self.AB) * (self.p/2 - self.BC) * (self.p/2 - self.AC))
        return f'Площадь равна - {round(self.s)}'

    def height(self):
        """Вычисляем высоту"""
        self.distance()
        self.area()
        self.h = 2 * (self.s / self.AC)
        return f'Высота равна - {self.h}'

trian = Triangle(5, 2, 7, 3, 5, 7)
print(trian.distance())
print(trian.perimeter())
print(trian.area())
print(trian.height())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

        self.AB = round(sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2))
        self.BC = round(sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2))
        self.CD = round(sqrt((self.x4 - self.x3) ** 2 + (self.y4 - self.y3) ** 2))
        self.AD = round(sqrt((self.x4 - self.x1) ** 2 + (self.y4 - self.y1) ** 2))

    def ravn(self):
        if self.AB == self.CD:
            return f'Это равнобедренная трапеция'
        else:
            return f'Это не равнобедренная трапеция'

    def distance(self):
        return f'Длинна AB - {round(self.AB)}\nДлинна BC - {round(self.BC)}\nДлинна CD - {round(self.CD)}\nДлинна AD - {round(self.AD)}'

    def perimeter(self):
        self.P = self.AB + self.BC + self.CD + self.AD
        return f'Периметр трапеции - {round(self.P)}'

    def area(self):
        self.S = ((self.AB + self.BC)/2)*sqrt(self.CD ** 2 - ((self.AB - self.BC)/4))
        return f'Площадь трапеции - {round(self.S)}'

trap = Trapeze(5, 2, 7, 3, 5, 7, 6, 9)
print(trap.ravn())
print(trap.distance())
print(trap.perimeter())
print(trap.area())
