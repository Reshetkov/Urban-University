from threading import Thread
import queue
from random import randint
import time

class Table:
    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        t = randint(3, 10)
        time.sleep(t)

class Cafe:
    def __init__(self, queue, *tables):
        pass

    queue = queue.Queue()
    def guest_arrival(self, *guests):
        for guest in guests:
            for table in tables:
                self.list = []
                if table.guest is None:
                    table.guest = guest
                    table.guest.start()
                    print(f'{table.guest.name} сел(-а) за стол номер {table.number}')
                    self.list.append(guest.name)
                    break
            if guest.name not in self.list:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest != None for table in tables):
            for table in tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if not self.queue.empty() and table.guest == None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()