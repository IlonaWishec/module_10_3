import  threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            random_plus = random.randint(50, 500)
            self.balance += random_plus
            print(f'Пополнение: {random_plus}. Баланс: {self.balance}.')
            if self.balance >= 500 and self.lock.locked == True: # и замок заблокирован
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            random_minus = random.randint(50,500)
            print(f'Запрос на {random_minus}.')
            if random_minus <= self.balance:
                self.balance -= random_minus
                print(f'Снятие: {random_minus}. Баланс: {self.balance}.')
            else:
                print('Запрос отклонен, недостаточно средств.')
            self.lock.acquire()

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
