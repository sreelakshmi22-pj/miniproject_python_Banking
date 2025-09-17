# find the bank balance after deposit and withdraw

class BankAccount:
    def __init__(self, name, account_number, balance):
        self.__account_numer = account_number
        self.__balance = balance
        self.__name = name

    def personal_bank_info(self):
        print("name is :", self.__name)
        print("account number :", self.__account_numer)
        print("balance is:", self.__balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"deposited : {amount}, new balance :{self.__balance}")
        else:
            print("deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"withdraw :{amount},new balance :{self.__balance}")
        else:
            print("invalid amount")


obj = BankAccount("philip", 100, 50000)
obj.personal_bank_info()
obj.deposit(50000)
obj.withdraw(50000)