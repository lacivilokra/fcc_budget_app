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
        self.description = description
        withdraw_funds = amount * -1
        depo = {'amount' : withdraw_funds, 'description': self.description}
        self.ledger.append(depo)

    def get_balance():
        return(self.balance)


        





        