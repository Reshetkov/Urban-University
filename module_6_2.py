class Vehicle:
    __COLOR_VARIANTS = ['green', 'white', 'black']
    def __init__(self, owner, model, engine_power, color):
        self.owner = owner # публичный атрибут
        self.__model = model # приватный атрибут
        self.__engine_power = engine_power
        self.__color = color
    def get_model(self):
        return (f'Модель: {self.__model}')
    def get_horsepower(self):
        return (f'Мощность двигателя: {self.__engine_power}')
    def get_color(self):
        return (f'Цвет: {self.__color}')

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')
        print(self.__model) # а изнутри класса мы можем обращаться к модели, т.к. это приватный атрибут и к нему есть доступ


    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle = Sedan('Alex', '2024', 250, 'green')
vehicle.print_info()
vehicle.set_color('red')
vehicle.set_color('BLACK')
vehicle.owner = 'Пётр'
vehicle.print_info()
print(vehicle.owner)  # к owner можно обращаться извне класса, т.к. это публичный атрибут и к нему есть доступ
#print(vehicle.__model) # мы не можем обращаться к модели извне класса, т.к. это приватный атрибут и к нему нет доступа