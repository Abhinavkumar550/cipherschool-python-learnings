class student:
    total_students=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        student.total_students += 1
    def hello(self):#we have to use self otherwise it wont work 
        print("Hello",self.name)
    @staticmethod
    def college_name():
        print("Welcome:")
s1=student("Abhinav",2500000)
s2=student("Prem",2)
#print(s1.name,s1.salary)
	#print(s2.name,s2.salary)
#print(student.total_students)
s1.hello()
s2.hello()
s1.college_name()

