class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
        self.withdraw_funds = 0
    
    def deposit(self, amount, description = ''):
        self.balance += amount
        if description:
            self.ledger.append({'amount' : amount, 'description' : description})
        else:
            self.ledger.append({'amount' : amount, 'description' : ''})

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
            self.withdraw(amount, 'Transfer to ' + category.name)
            self.deposit(amount, 'Transfer from ' + self.name)
            return True

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

    def __str__(self):
        title = self.name.center(30, '*')
        items = ''
        for i in self.ledger:
            items += f"{i['description'][0:23]:23}" + f"{i['amount']:>7.2f}" + '\n'

        output = title + '\n' + items + 'Total: ' + str(self.balance)
        return output

def create_spend_chart(categories):
    all_cat = []
    spent_all_cat = []
    perc_all_cat = []

    for c in categories:
        total_spent = 0
        all_cat.append(c.name)
        for x in c.ledger:
            if x['amount'] < 0:
                total_spent -= x['amount']
        spent_all_cat.append(total_spent)
    for x in spent_all_cat:
        percent = round(x / sum(spent_all_cat), 2) * 100
        perc_all_cat.append(percent)
    
    chart = 'Percentage spent by category\n'
    bars = range(100, -10, -10)
    for b in bars:
        chart += str(b).rjust(3) + '| '
        for x in perc_all_cat:
            if x >= b:
                chart += 'o  '
            else:
                chart += '   '
        chart += '\n'
    chart += '    ----' + '---' * (len(all_cat) -1) + '/n     '

    longest_length = len(all_cat[0])

    for x in all_cat:
        if len(x) > longest_length:
            longest_length = len(x)
    for x in range(longest_length):
        for y in all_cat:
            if x < len(y):
                chart += y[x] + '  '
            else:
                chart += '   '
        if x < longest_length -1:
            chart += '\n     '
    return chart
    

            






        





        