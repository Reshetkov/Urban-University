import threading
from threading import Lock
from random import randint
import time

lock = Lock()
class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self):
        for i in range(100):
            plus = randint(50, 500)
            self.balance += plus
            if self.balance >= 500 and lock.locked() == True:
                lock.release()
            print(f'Пополнение: {plus}. Баланс: {self.balance}')
            time.sleep(0.001)
        return self.balance
    def take(self):
        for i in range(100):
            minus = randint(50, 500)
            print(f'Запрос на {minus}')
            if minus <= self.balance:
                self.balance -= minus
                print(f'Снятие: {minus}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                lock.acquire()
        return self.balance

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')