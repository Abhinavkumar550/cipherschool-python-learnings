student={}
while True:
    print("1.Add Student")
    print("2.View all Student")
    print("3.Search Student")
    print("4.Delete Student")
    print("5.Exit")
    choice=input("Enter your choice:")
    if choice=="1":
        roll=int(input("Enter the roll no"))
        name=input("Enter your name:")
        course=input("Enter your course")
        student[roll]={"name":name,"course":course}
        print("Student data added Successfully")
    if choice=="2":
        if students:
            print("\nall students:")
            for roll,info in student.items():
                print("Roll:",roll)
                print("name",info["name"])
                print("course:",info["course"])
        else:
            print("no student record found")
    elif choice=="3":
        roll=input("Enter the rooll nnumber to search:")
        if roll in students:
            print("Name:",students[roll]["name"])
            print("course:",students[roll]["course"])
        else:
            print("Student not found")
    elif choice=="4":
        roll=input("enter the roll number")
        removed=student.pop(roll,"not found")
        if removed=="not found":
            print("Stundet not found")
        else:
            print("Stundet deletd sauccessfully ")
    elif choice == "5":
        print('Thank you for using student record')
    else:
        print("invalid choice")
