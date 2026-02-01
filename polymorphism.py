#Polymorphism
class truck:
    def write(self):
        print("truck is moving ")
class car:
    def write(self):
        print("car is moving ")
class bike:
    def write(self):
        print("bike is moving")
h=truck()
b=car()
d=bike()
h.write()
b.write()
d.write()
#create a class person  with a perspn with a method roll and then create studetn and tracher inheriting person class
#studetn-print(i am student)
#teacher- print(i am teachetr)
#create another clkASS ASSITANT THAT INHERITS from both styudet and teacher
#1 create and object of assistant
#2call role()
#3. obseerve whisch method is called


class person:
    def roll(self):
        print("person")
class student(person):
    print("I am student ")
class teacher(person):
    print("I am teacher")
#s1=assitant()
#s1.roll()

#reference and object behaviour
#b=a
#b.append(4)
#print(a)

class person:
    def roll(self):
        print("I am, person")
class student(person):
        print("I am student")
class teacher (person):
    print("I am teacher")
class assitant(student,teacher):
    pass
r1=assitant
r1.roll()

