#create a bankaccount class
class BankAccount():

    #use a classmethod to print all instances of a Bank Account's info
    all_bank_acc_info = []

    def __init__(self, int_rate = .01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_bank_acc_info.append(self)
    
    @classmethod
    def all_bals(cls):
        sum = 0
        for account in cls.all_bank_acc_info:
            sum += account.balance
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds, sucka!: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance *= 1 + self.int_rate
        
        return self

b_a1 = BankAccount()
b_a2 = BankAccount()

b_a1.deposit(1882).deposit(1873).deposit(1885).withdraw(230).yield_interest().display_account_info()

b_a2.deposit(1650).withdraw(270).withdraw(450).withdraw(649).withdraw(480).yield_interest().display_account_info()


# for info in BankAccount.all_bank_acc_info:
#     print(BankAccount.all_bank_acc_info[info])