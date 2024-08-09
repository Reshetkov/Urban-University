class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self):
        if new_floor <= self.number_of_floors and new_floor > 0:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')
h1 = House('ЖК1', 5)
h2 = House('ЖК2', 10)


new_floor = int(input('Введите номер этажа, на который нужно приехать: '))
h1.go_to()
h2.go_to()