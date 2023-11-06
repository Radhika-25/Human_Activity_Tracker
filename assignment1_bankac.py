class BankAccount():
    def __init__(self, num, name, bal):
        self.account_number = num
        self.account_holder_name = name
        self.account_balance = bal

    def deposit(self, deposit_amount):
        if(deposit_amount >=0):
            self.account_balance = self.account_balance + deposit_amount
            print(f"New balance = {self.account_balance}.")
        else:
            print("The deposit amount must be positive.")
    
    def withdraw(self, withdraw_amount):
        if(withdraw_amount>=0 and withdraw_amount< self.account_balance):
            self.account_balance = self.account_balance - withdraw_amount
            print(f"New balance = {self.account_balance}.")
        else:
            print("Error!!!")
            print("Amount to be withdrawn can be positive only. Also,an amount greater than your current balance cannot be withdrawn.")

    def check_balance(self):
        print(f"The current account balance of account {self.account_number} is {self.account_balance}.")

class SavingsAccount(BankAccount):
    def __init__(self, num, name, bal):
        super().__init__(num, name, bal)
    def withdraw(self, withdraw_amount):
        if((self.account_balance - withdraw_amount)>500 and withdraw_amount>0):
            self.account_balance = self.account_balance - withdraw_amount
            print(f"New balance = {self.account_balance}.")
        else:
            print("Error!!!")
            print("Amount to be withdrawn can be positive only. Also,account must have a minimum threshold amount of Rs.500")
    
class update(BankAccount):
    def new_name(self, newname):
        self.account_holder_name = newname
        print(f"The name has been updated to {self.account_holder_name}")

ac1 = BankAccount( 789, "Saraswati", 45000)
ac1.check_balance()
ac1.deposit(1000)
ac1.withdraw(5000)
ac1 = SavingsAccount(789, "Saraswati", 45000)
ac1.check_balance()
ac1.withdraw(47000)
ac1 = update(789, "Saraswati", 45000)
ac1.new_name("Lakshmi")
print(ac1.account_holder_name)
