#create a class banck balance in which balance is hidden 
class bank:
    def __init__(self,balance):
        self.__balance=balance
    def get_balance(self):
        return self.__balance

    def withdraw(self):
        a=int(input("enter the amount you want to withdraw:"))
        if(self.__balance>a):
            self.__balance=self.__balance-a
    def set_balance(self,deposit):
        deposit=int(input("Enter the value: "))
        self.__balance=self.__balance+deposit

s1=bank(12000)
s1.withdraw()
s1.set_balance()
print(s1.get_balance())

