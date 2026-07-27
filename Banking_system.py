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

class CheckingAccount(Account):
    def __init__(self, account_number, holder_name, initial_balance, overdraft_limit=0):
        super().__init__(account_number, holder_name, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount): 
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded")
        
        self._Account__balance -= amount  
        print(f"Withdrawn ${amount}. Updated Balance: ${self.balance}")

    def display_account_info(self):
        super().display_account_info()
        print(f"Overdraft Limit : ${self.overdraft_limit}")


class Bank:
    def __init__(self):
        self.accounts = {} 
    
    def add_account(self, account_obj):
        self.accounts[account_obj.account_number] = account_obj
        print(f"Account {account_obj.account_number} added successfully.")

    def transfer_funds(self, from_acc_no, to_acc_no, amount):
        if from_acc_no not in self.accounts:
            raise ValueError("Sender account not found")
        if to_acc_no not in self.accounts:
            raise ValueError("Receiver account not found")
        
        from_account = self.accounts[from_acc_no]
        to_account = self.accounts[to_acc_no]
        
        try:
            from_account.withdraw(amount) 
            to_account.deposit(amount)
            print(f"Transferred ${amount} from {from_acc_no} to {to_acc_no}")
        except ValueError as e:
            print(f"Transfer failed: {e}")

   
    def audit_accounts(self):
        print("\n========== BANK AUDIT ==========")
        for acc_no, account in self.accounts.items():
            account.display_account_info() 
            print("-" * 30)

if __name__ == "__main__":
  
    bank = Bank()

    acc1 = SavingsAccount("ACC101", "Sara Khan", 10000, 5)
    acc2 = CheckingAccount("ACC202", "Ali Ahmed", 2000, overdraft_limit=1000)

    
    bank.add_account(acc1)
    bank.add_account(acc2)

    print("\n----- Banking System Test -----")

    acc1.deposit(2000)
    acc1.apply_interest()
    
    acc2.withdraw(2500)

    bank.transfer_funds("ACC101", "ACC202", 1000) 

    bank.audit_accounts()
