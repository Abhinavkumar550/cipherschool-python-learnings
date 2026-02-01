class parent:
    def __init__(self):
        self._x=10   # normal x is public _x is protected(can acces within class and in python you can access outside but it will give warning) and __x is private
class child(parent):
    def show(self):
        print(self._x)
obj=child()
obj.show()
#print(obj._x)

class person:
    def __init__(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
class student(person):
    def show_name(self):
        print("my name is",self.get_name())
s1=student("Abhinav")
s1.show_name()
#create a parent class account it shoudl have proteted variable _balance then constrictor should set the balance ,method show_balance() should print balance it shoul be in parent class
#child class saving_account inherit from account the  create a methoid add_money(amount) add amount to baloance and how updated ba;ance

class account:
    def __init__(self,balance):
        self._balance=balance
    def show_balance(self):
        return self._balance
class saving_account(account):
    def add_money(self,amount):
        amount=int(input("Enter the value :"))
        self._balance=self._balance+amount
s1=saving_account(1000)
s1.show_balance()

