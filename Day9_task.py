class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be > 0")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw must be > 0")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    def show_details(self):
        print(f"Holder: {self.account_holder}, Balance: {self.__balance}")

acc = BankAccount("Fajar", 5000)
acc.show_details()

acc.deposit(2000)
acc.show_details()

acc.withdraw(1000)
acc.show_details()

try:
    acc.deposit(-100)
except ValueError as e:
    print(e)

try:
    acc.withdraw(10000)
except ValueError as e:
    print(e)

try:
    acc.balance = -50
except ValueError as e:
    print(e)

try:
    print(acc.__balance)
except AttributeError as e:
    print(e)