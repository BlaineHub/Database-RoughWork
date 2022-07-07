####Base Class####
class Account:
    '''This is the base class'''
    def __init__(self,filepath):
        self.filepath = filepath
        with open(filepath,'r') as file:
           self.balance = int(file.read())

    def withdraw(self,amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    '''This class generates checking account objects'''
    type = 'checking'
    def __init__(self,filepath, fee):
        Account.__init__(self,filepath)
        self.fee = fee

    def transfer(self,amount):
        self.balance=self.balance - amount - self.fee

jacks_checking=Checking('oop_practice/jacks_balance.txt',1)
jacks_checking.transfer(0)
jacks_checking.commit()
print(jacks_checking.balance)
print(jacks_checking.type)

johns_checking=Checking('oop_practice/johns_balance.txt',1)
johns_checking.transfer(0)
johns_checking.commit()
print(johns_checking.balance)
print(johns_checking.type)

print(johns_checking.__doc__)

