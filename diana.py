import math
class Figure:
    sides_count = 0
    def __init__(self, color, sides, filled):
        self.__color = color
        self.__sides = sides
        self.filled = filled

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r: int, g: int, b: int):
        if 0 < r < 250 and 0 < g < 250 and 0 < b < 250:
            return True
        else:
            return False
    def set_color(self, r: int, g: int, b: int):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
    def __is_valid_sides(self, *sides):
        sited_spisok = []
        for i in sides:
            if i > 0:
                sited_spisok.append(i)
            if i > 0 and sited_spisok == self.__sides:
                return True
            else:
                return False
    def get_sides(self):
        return (self.__sides)
    def __len__(self):
        return sum(self.__sides)
    def set_sides(self, *new_sides):
        self.__sides = new_sides
        if self.sides_count != len(self.__sides):
            return self.__sides
        else:
            return self.__sides
class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *sides):
        super().__init__(color, sides, filled = True)
        self.__radius = Figure.__len__(self) / (2*math.pi)
    def get_square(self):
        import math
        rad = self.__radius**2 * math.pi
        return rad
class Triangle(Figure):
    sides_count = 3
    def __init__(self, __color, __sides: int,  filled='bool'):
        super().__init__(__color, __sides, filled)
    def get_square(self):
        square = 1 / 2 * sum(self.__sides)
        return square
# class Cube(Figure):
#     sides_count = 12
#
#     """ Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)"""
#
#     def __init__(self, __color, __sides: int, filled='bool'):
#         super().__init__(__color, __sides,  filled)
#         # for i in len(self.__sides):
#         #     if
#         # if len(__sides) == 1:
#         #     self.__sides = self.sides_count * [i for i in __sides]
#         # else:
#         #     self.__sides = [1 * self.sides_count]
#
#     def get_volume(self):
#         return self.__sides * 3
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
# cube1 = Cube((222, 35, 130), 6)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
# cube1.set_color(300, 70, 15) # Не изменится
# print(cube1.get_color())
# Проверка на изменение сторон:
# cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
# print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
# Проверка периметра (круга), это и есть длина:
print(len(circle1))
# Проверка объёма (куба):
# print(cube1.get_volume())