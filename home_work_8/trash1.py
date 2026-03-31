# Цель: отработать работу с классами, наследованием и обработкой исключений в Python.
#
# Шаг 1. Создайте базовый класс BankAccount:
#
# Атрибуты: owner (имя владельца), balance (баланс, по умолчанию 0).
#
# Методы:
#
# deposit(amount) — пополняет счёт. Если amount ≤ 0, выбрасывает ValueError с сообщением «Сумма пополнения должна быть положительной».
#
# withdraw(amount) — снимает деньги. Если amount > balance, выбрасывает InsufficientFundsError (пользовательское исключение).
#
# get_balance() — возвращает текущий баланс.
#
# Шаг 2. Определите пользовательское исключение InsufficientFundsError, наследующее от Exception, с сообщением по умолчанию «Недостаточно средств на счёте».
#
# Шаг 3. Создайте класс‑наследник SavingsAccount, который наследует BankAccount:
#
# Добавьте атрибут interest_rate (процентная ставка, по умолчанию 0.05).
#
# Переопределите метод withdraw(amount): если сумма снятия превышает 80 % от баланса, выбрасывайте Exception с сообщением «Нельзя снять более 80 % за раз».
#
# Добавьте метод apply_interest(), который увеличивает баланс на balance × interest_rate.
#
# Шаг 4. Напишите функцию process_operations(account, operations), которая:
#
# Принимает объект счёта и список операций вида ('deposit', 100) или ('withdraw', 50).
#
# Для каждой операции использует try/except, чтобы перехватить любые исключения.
#
# При перехвате выводит сообщение: «Ошибка: {текст ошибки}».
#
# В конце выводит итоговый баланс через get_balance().

class BankAccount:

    def __init__(self, owner: str, balance: int = 0):
        self.owner = owner
        self.balance = balance
        print(f'Создан {owner} с балансом {balance}')

    def deposit(self, amount:int):
        try:
            if amount <= 0:
                raise ValueError("Сумма пополнения должна быть положительной")
            self.balance = self.balance + amount
            print(f"Счёт пополнен на {amount} единиц")
        except ValueError:
            raise

    def withdraw(self, amount:int):
        try:
            if amount <= 0:
                raise ValueError("Сумма снятия должна быть положительной")
            if amount > self.balance:
                raise ValueError("Недостаточно средств на счёте для снятия")
            self.balance -= amount
            print(f"Счёт снизился на {amount} единиц")
        except ValueError:
            raise
    def get_balance(self):
        print(f'Текущий баланс = {self.balance}')

v1 = BankAccount('v1', 300)
v1.deposit(100)
v1.withdraw(30)
v1.get_balance()
