import time
from threading import Thread

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        self.days_battle = 0
        self.num_warrior_left = 100
        print(f'{self.name}, на нас напали!')

        while self.num_warrior_left > 0 and self.num_warrior_left >= self.power:
            self.days_battle += 1
            self.num_warrior_left -= self.power
            print(f'{self.name} сражаетcя {self.days_battle} день(дня)..., осталось {self.num_warrior_left} воинов.')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {self.days_battle} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')