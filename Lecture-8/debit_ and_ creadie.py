# Creat Account class with 2 attributes - balance and account no.
# Creat methods for debit, credit and printing the balance


class account:
    def __init__(self,Account_number,balance):
        self.Account_number = Account_number
        self.balance = balance
        print(f"Your Account Number is : {self.Account_number}.\nYour Balance Is : {self.balance }")
    def debit(self,amount):
        if amount > self.balance:
             print("insuuficent Balance")
        else:
            self.balance -= amount
            print("Your debit Balance is",amount)
            print("Total amount is",self.get_balance())
           
    def creadit(self,Amount):
         self.balance += Amount
         print("Your creadit Balance is",Amount)
         print("Total amount is",self.get_balance())
                     
    def get_balance(self):
        return self.balance
    

s = account(764767835424,100000)
s.debit(6895)
s.creadit(758)
    



