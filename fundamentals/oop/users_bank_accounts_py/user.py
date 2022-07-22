from bank_account import BankAccount

# create a user class
class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = BankAccount()


    #have this method print all of the users details on separated lines
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self

    #have this method change the user';s member status to True and set their gold card points to 200
    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member.")
        else:
            self.gold_card_points = 200
            self.is_rewards_member = True
        return self

    #have this method decrease the user's points by the amount specified
    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
        else:
            self.gold_card_points = 0
        return self
    #calls on the bank accounts instance method deposit
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    #calls on the bank accounts instance method withdraw
    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

beth_user = User("Beth", "B", "bb@b.com", 100)

# beth_user.display_info()

beth_user.display_info().enroll().spend_points(50).display_info()
beth_user.enroll().display_info().display_user_balance().make_deposit(10).display_user_balance()


# print(beth_user.is_rewards_member)

# beth_user.display_info()
# beth_user.spend_points(50)
# beth_user.display_info()