class parent:
    def shape(self):
        print("this is shape")
class child(parent):
    def shape(self):
        print("this is circle")
    def __init__(self):
        super().__init__()
        print("this is child constructor")
        
obj=child()
obj.shape()
#two class teacher i whioch we have to [rint tracong an then coder in which coding in last which will inherit both student pass
class teacher:
    def teaching(self):
        print("teaching is good ")
class coder:
    def coding(self):
        print("coding is good too ")
class student(teacher,coder):
    pass
s1=student()
s1.coding()
s1.teaching()

class parent:
    def __init__(self):
        self.__x=10
class child(parent):
    def show(self):
        print(self._parent__x)
obj=child()
obj.show()
class teacher:
    def teaching(self):
        print("Teacher is randi wala")
class coder:
    def coding(self):
        print("This is coding class")
class student(teacher,coder):
    pass
r1=student()
r1.coding()
r1.teaching()

    
