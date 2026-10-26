class Bank:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        # Modifies the private balance inside the if-else blocks
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Modifies the private balance inside the if-else blocks
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display(balance):
        print("Balance amount is INR ")