class Animal:
    def __init__(self, name, alive = True, fed = False):
        self.name = name
        self.alive = alive
        self.fed = fed
    def eat(self, food):
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        if food.edible == False:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
class Plant:
    edible = False
    def __init__(self, name):
        self.name = name
class Mammal(Animal):
    pass
class Predator(Animal):
    pass
class Flower(Plant):
    pass
class Fruit(Plant):
    edible = True

a1 = Predator('Тигр')
a2 = Mammal('Конь')
p1 = Flower('Роза')
p2 = Fruit('Апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)