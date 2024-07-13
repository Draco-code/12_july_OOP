class Account:
    def __init__(self, id: str, name: str, balance: int = 0) -> None:
        self.id = id
        self.name = name
        self.balance = balance

    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_balance(self):
        return self.balance
    
    def credit(self, amount: int):
        self.balance += amount
        return f'Current balance: {self.balance}'  
      
    def debit(self, amount: int):
        if self.balance >= amount:
            self.balance -= amount
            return f'Current balance: {self.balance}'
        else:
            print("Amount exeeded balance!")
            return self.balance

    def transferTo(self, accountName: str, amount: int):
        """transfer money to another account"""
        if self.balance >= amount:
            self.balance -= amount
            accountName.balance += amount
            return f'Current balance: {self.balance}'
        else:
            print("Amount exeeded balance!")
            return self.balance
        
    def toString(self):
        return f"Id : {self.get_id()}, name: {self.get_name()}, balance: {self.get_balance()}]"
    

u1 = Account('1234', 'asadulloh', 1000)
u2 = Account('4321', 'Begzod')

print(u1.transferTo(u2, 200))
print(u2.get_balance())
    