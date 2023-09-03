from bank import BankAccount


class User():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account = BankAccount(int_rate=0.02, balance=balance)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        self.account.display_account_info()

    def transfer_money(self, other_user, amount):
        if amount > self.account.balance:
            print("Insufficient funds for transfer")
        else:
            self.account.balance -= amount
            other_user.account.balance += amount
            print(f"{self.name} transferred {amount} to {other_user.name}")
        return self

    def make_deposit(self, amount):
        self.account.deposit(amount)


guido = User("Test", 650)
guido.make_withdrawal(70)
guido.make_deposit(50)
guido.display_user_balance()
