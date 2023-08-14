class BankAccount:
    bankAccounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.bankAccounts.append(self)

    def deposit(self, amount):
        self.amount = amount
        self.balance += float(amount)
        return self.balance

    def withdraw(self, amount):
        self.amount = amount
        self.balance -= float(amount)
        return self.balance

    def display_account_info(self):
        print(f"You have ${self.balance} in your bank account")

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.int_rate
        else:
            print(f"The balance is negative. Balance: ${self.balance}")

        return self.balance

    @classmethod
    def printInstances(cls):
        for account in cls.bankAccounts:
            print(
                f"The balance is: {account.balance} and interest rate is: {account.int_rate}")


kristisAccount = BankAccount(1.2, 4000)
kristisAccount.deposit(500)
kristisAccount.deposit(1000)
kristisAccount.deposit(50.50)
kristisAccount.withdraw(600)
kristisAccount.yield_interest()
kristisAccount.display_account_info()

anotherAccount = BankAccount(0.8, 1000)
anotherAccount.deposit(1000)
anotherAccount.deposit(1000)
anotherAccount.withdraw(500)
anotherAccount.withdraw(400)
anotherAccount.withdraw(600)
anotherAccount.withdraw(500)
anotherAccount.yield_interest()
anotherAccount.display_account_info()

BankAccount.printInstances()
