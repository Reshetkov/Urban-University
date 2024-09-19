first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, 'a')
        for i in range (len(data_set)):
            file.write(str(data_set[i]))
            file.write('\n')
        file.close()
    return write_everything
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

from random import choice
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        self.choice = choice(self.words)
        return self.choice

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())