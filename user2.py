class User:
    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount
        return self

    def make_withdrawal(self,amount):
        self.amount = amount
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self
    
    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()

lisa = User("Lisa")

lisa.make_deposit(100).make_deposit(200).make_deposit(120).make_withdrawal(200)
lisa.display_user_balance()

will = User("Will")
will.make_deposit(200).make_deposit(250).make_withdrawal(100).make_withdrawal(150)
will.display_user_balance()

kai = User("Kai")
kai.make_deposit(120).make_withdrawal(20).make_withdrawal(20).make_withdrawal(10)
kai.display_user_balance()

kai.transfer_money(140, will)