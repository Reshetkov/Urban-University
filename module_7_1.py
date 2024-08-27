class Product:
    def __init__(self, name, weight, category):   # строка, дробное число (5.4, 52.8 и т.п.), строка
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop():
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        self.list_temp = file.read()
        file.close()
        return (self.list_temp)

    def add(self, *products):
        for i in range(len(products)):
            file = open(self.__file_name, 'r')
            if str(products[i]) in self.get_products():
                print(f'Продукт {products[i]} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(str(products[i]))
                file.write('\n')
            file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())