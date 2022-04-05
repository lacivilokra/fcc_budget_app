class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = ()
        self.balance = 0
        self.withdraw_funds = 0
    
    def deposit(self, amount, description = ''):
        self.balance += amount
        self.description = description
        depo = {'amount' : amount, 'description' : self.description}
        self.ledger.append(depo)

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount) == False:
            return False
        else:
            self.description = description
            withdraw_funds = amount * -1
            depo = {'amount' : withdraw_funds, 'description': self.description}
            self.ledger.append(depo)
            self.balance += withdraw_funds
            self.withdraw_funds += withdraw_funds
            return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount) == False:
            return False
        else:
            self.withdraw(amount, 'Transfer to {}'.format(category.name))
            self.deposit(amount, 'Transfer from {}'.format(self.name))
            return True

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

    def __str__(self):
        title = self.name.center(30, '*')

def create_spend_chart()







        





        