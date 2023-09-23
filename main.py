
# Создать класс Triangle с полями-сторонами. Определить методы изменения сторон,
# вычисления углов, вычисления периметра. Создать произвольный класс Equilateral
# (равносторонний), имеющий поле площади. Определить метод вычисления площади.

class Triangle:

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def __str__(self):
        return (f'Side one: {self.side1}\n'
                f'Side two: {self.side2}\n'
                f'Side three: {self.side3}')

    def count_p(self):
        return self.side1 + self.side2 + self.side3

    def set_side_one(self, new_side_one):
        self.side1 = new_side_one
    def get_side_one(self):
        return self.side1

    def set_side_two(self, new_side_two):
        self.side2 = new_side_two
    def get_side_two(self):
        return self.side2

    def set_side_three(self, new_side_three):
        self.side3 = new_side_three
    def get_side_three(self):
        return self.side3

class Equilateral(Triangle):
    def __init__(self, side1, side2, side3, area):
        super().__init__(side1, side2, side3)
        self.area = area

# Площадь равностороннего треугольника можно найти следующим образом:
# S = a * h / 2, где h – это высота. Высоту можно вычислить, используя теорему
# Пифагора: h = а² - (а / 2)².

    def area_equilateral(self):
        h = self.side1 ** 2 - (self.side1 / 2) ** 2
        s = self.side1 * h / 2
        return s


s1 = int(input('Enter side one: '))
s2 = int(input('Enter side two: '))
s3 = int(input('Enter side three: '))
print('----------------')

triangle = Triangle(s1, s2, s3)
print(triangle)
print('----------------')

triangle.set_side_one(10)
print(triangle.get_side_one())

triangle.set_side_two(15)
print(triangle.get_side_two())

triangle.set_side_three(11)
print(triangle.get_side_three())
print('----------------')

s4 = int(input('Enter the sides of equilateral triangle: '))
ar = int(input('Enter the area: '))
print('----------------')

equilateral = Equilateral(s4, s4, s4, ar)
print(equilateral)
print('----------------')

print(f'Perimeter of triangle: {triangle.count_p()}')
print('----------------')
print(f'Perimeter of equilateral: {equilateral.count_p()}')

print(f'Area of equilateral: {equilateral.area_equilateral()}')






