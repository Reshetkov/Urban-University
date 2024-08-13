class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if not isinstance(value, int):
            raise ArithmeticError('Правый операнд должен быть целым числом')
        return House(self.name, self.number_of_floors + value)

    def __radd__(self, value):
        if not isinstance(value, int):
            raise ArithmeticError('Правый операнд должен быть целым числом')
        return self + value

    def __iadd__(self, value):
        if not isinstance(value, int):
            raise ArithmeticError('Правый операнд должен быть целым числом')
        return self + value

h1 = House('ЖК1', 5)
h2 = House('ЖК2', 10)

print(h1)
print(h2)
print(h1 == h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 != h2)
h1 = h1 + 2
print(h1)
h1 = 2 + h1
print(h1)
h1 += 2
print(h1)