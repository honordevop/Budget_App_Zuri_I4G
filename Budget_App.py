class Budget:

    def __init__(self, category, deposit, withdraw, transfer, check_balance):
        self.category = category
        self.deposit = deposit
        self.withdraw = withdraw
        self.transfer = transfer
        self.check_balance = check_balance

    def deposit1(self):
        print(f'# {self.deposit} was deposited into {self.category} category')
        # amount = int(input("How much do you want to deposite:  "))
        # deposit= deposit + amount
    
    def withdraw1(self):
        print(f'# {self.withdraw} was withdraw from {self.category} category')
    
    def checkBalance(self):
        print(f'The balance for {self.category} category is # {self.check_balance}')
    
    def transfer1(self):
        print(f' # {self.transfer} was trasfered from {self.category} category')

food = Budget('food', 2000, 100, 50, 1000)
clothing = Budget('clothing', 30000, 1200, 4200, 1000)
Entertainment = Budget('entertainment', 12000, 1100, 5050, 1000)
Data = Budget('data', 10000, 1000, 500, 8000)
print('***********************FOOD CATEGORY*****************************')
food.deposit1()
food.withdraw1()
food.checkBalance()
food.transfer1()
print('***********************CLOTHING CATEGORY*****************************')
clothing.deposit1()
clothing.withdraw1()
clothing.checkBalance()
clothing.transfer1()
print('***********************DATA CATEGORY*****************************')
Data.deposit1()
Data.withdraw1()
Data.checkBalance()
Data.transfer1()
