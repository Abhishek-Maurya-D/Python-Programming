# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance

class Account:
    def __init__(self, bal, acc_no):
        self.balance = bal
        self.account_no = acc_no

    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.",amount,"was debited")
        print("Total balance = ",self.get_balance())

    # Credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.",amount,"was Credited")
        print("Total balance = ",self.get_balance())

    #Balance printing
    def get_balance(self):
        return self.balance

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)