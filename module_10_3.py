import threading
import random
import time
class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
    def deposit(self):

        for i in range(100):
            time.sleep (0.001)
            balance_app = random.randint (50, 500)
            self.balance += balance_app
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
                print("Освобожден")
            print(f"Пополнение: {balance_app}. Баланс: {self.balance}")


    def take(self):
        for b in range(100):
            balance_app = random.randint (50, 500)
            print (f"Запрос на {balance_app}")
            if balance_app <= self.balance:
                self.balance -= balance_app
                print(f"Снятие: {balance_app}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            time.sleep (0.001)

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()
th1.join()
th2.join()
balance1 =bk.balance
print(f'Итоговый баланс: {balance1}')