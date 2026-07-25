
class Account:
    def __init__(self, account_number, holder_name, initial_balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.__balance = initial_balance  

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):

        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value

    def deposit(self, amount):
    
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. Updated Balance: ${self.__balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.__balance:
            raise ValueError("Insufficient funds")
        else:
            self.__balance -= amount
            print(f"Withdrawn ${amount}. Updated Balance: ${self.__balance}")

    def display_account_info(self):
        
        print("\n--- Account Information ---")
        print(f"Account Number : {self.account_number}")
        print(f"Account Holder : {self.holder_name}")
        print(f"Current Balance: ${self.__balance}")
    


class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, initial_balance, interest_rate):
        super().__init__(account_number, holder_name, initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
    
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest  
        print(f"Interest of ${interest:.2f} applied @ {self.interest_rate}%")
        print(f"New Balance: ${self.balance:.2f}")


if __name__ == "__main__":
    acc = SavingsAccount("ACC101", "Sara Khan", 10000, 5)

    acc.display_account_info()
    acc.deposit(2000)
    acc.withdraw(500)
    acc.apply_interest()
    acc.display_account_info()