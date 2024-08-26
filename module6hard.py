import math
class Figure:
    sides_count = 0
    def __init__(self, color, sides, filled):
        self.__color = color
        self.__sides = sides
        self.filled = filled

    def get_color(self):
        return list(self.__color)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) == True: self.__color = (r, g, b)

    def __is_valid_color(self, r, g, b):
        return (r in range (0,255) and g in range (0,255) and b in range (0,255))

    def get_sides(self):
        return list(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides) == True:
            self.__sides = new_sides
            return(list(self.__sides))

    def __is_valid_sides(self, *new_sides):
        return(all(new_sides[i] > 0 for i in range(len(new_sides))) and self.sides_count == len(new_sides))

    def __len__(self):
        len = sum(self.__sides)
        return (len)

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *sides):
        super().__init__(color, sides, filled=True)
        self.__radius = Figure.__len__(self)/(2*math.pi)
    def get_square(self):
        self.square = math.pi*self.__radius**2
        return self.square

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides):
        super().__init__(color, sides, filled=True)

    def get_square(self, sides):
        self.__sides = sides
        p = Figure.__len__(self)
        a = self.__sides[1]
        b = self.__sides[2]
        c = self.__sides[3]
        self.square = math.sqrt(p*(p-a)*(p-b)*(p-c))
        return self.square
class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *sides):
        super().__init__(color, sides, filled=True)
        self.__sides = Figure.get_sides(self)
    def get_sides(self):
        for i in range(self.sides_count - 1):
            self.__sides.extend(Figure.get_sides(self))
        return self.__sides

    def get_volume(self):
        self.volume = (self.__sides[1])**3
        return self.volume

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

#Проверка объёма (куба):
#print(circle1.get_square())
print(cube1.get_volume())