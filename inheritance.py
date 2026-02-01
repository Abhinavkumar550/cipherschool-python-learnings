class human:
    def eat(self):
        print("Human eats")
class student(human):
    def study(self):
        print("student can eat too")
s1=student()
s1.study()
s1.eat()

class animal:
    def safe(self):
        print("all animal are safe ")
class dog(animal):
    @staticmethod
    def bark():
        print("dogs can bark")
s2=dog()
s2.bark()
s2.safe()

class nokia:
    def phone(self):
        print("this is nokia")
class samsung(nokia):
    def call(self):
        print("yes it can call")
    def internet(self):
        print("yes it has internet")
s1=samsung()
s1.call()
s1.internet()
s1.phone()
