class Account:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value # Fixed: indentation

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"Deposit successful. New Balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.balance:
            raise ValueError("Insufficient balance")
        else:
            self.balance = self.balance - amount
            print(f"Withdrawal successful. New Balance: ${self.balance:.2f}")

    def display_account_info(self):
        print("\n--- Account Information ---")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance:.2f}")

class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.deposit(interest)
        print(f"Interest of ${interest:.2f} applied @ {self.interest_rate}%")

class CheckingAccount(Account): # Task 1: Overdraft
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.balance + self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded")
        else:
            self.balance = self.balance - amount
            print(f"Withdrawal successful. New Balance: ${self.balance:.2f}")

    def display_account_info(self): 
        super().display_account_info()
        print(f"Overdraft Limit: ${self.overdraft_limit:.2f}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_number = input("Enter account number: ")
        if account_number in self.accounts:
            print("Account already exists")
            return
        name = input("Enter account holder name: ")
        try:
            balance = float(input("Enter starting balance: "))
            print("1. Savings Account")
            print("2. Checking Account")
            choice = input("Select account type: ")
            if choice == "1":
                rate = float(input("Enter interest rate: "))
                account = SavingsAccount(account_number, name, balance, rate)
            elif choice == "2":
                limit = float(input("Enter overdraft limit: "))
                account = CheckingAccount(account_number, name, balance, limit)
            else:
                print("Invalid choice")
                return
            self.accounts[account_number] = account
            print("Account created successfully")
        except ValueError:
            print("Please enter a valid number")

    def deposit_money(self):
        account_number = input("Enter account number: ")
        try:
            amount = float(input("Enter amount: "))
            account = self.accounts.get(account_number) 
            if account:
                account.deposit(amount)
            else:
                print("Account not found")
        except ValueError:
            print("Invalid amount")

    def withdraw_money(self):
        account_number = input("Enter account number: ")
        try:
            amount = float(input("Enter amount: "))
            account = self.accounts.get(account_number)
            if account:
                account.withdraw(amount)
            else:
                print("Account not found")
        except ValueError as e:
            print(f"Error: {e}")

    def transfer_funds(self):
        sender = input("Enter sender account number: ")
        receiver = input("Enter receiver account number: ")
        try:
            amount = float(input("Enter amount: "))
            if sender in self.accounts and receiver in self.accounts:
                self.accounts[sender].withdraw(amount) # Task 3: Constraints check
                self.accounts[receiver].deposit(amount)
                print("Transfer successful")
            else:
                print("Account not found")
        except ValueError as e:
            print(f"Transfer failed: {e}")

    def view_account(self):
        account_number = input("Enter account number: ")
        account = self.accounts.get(account_number)
        if account:
            account.display_account_info()
        else:
            print("Account not found")

def main():
    bank = Bank()
    while True:
        print("\n----- Banking System -----")
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Funds")
        print("5. View Account Details")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            bank.create_account()
        elif choice == "2":
            bank.deposit_money()
        elif choice == "3":
            bank.withdraw_money()
        elif choice == "4":
            bank.transfer_funds()
        elif choice == "5":
            bank.view_account()
        elif choice == "6":
            print("Thank you for using Banking System")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
