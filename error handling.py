try:
    #risky code
    #a=int(input("Enter the number:"))
    #b=int(input("Enter the number : "))
    #print(a/b)
    file=open("movies1.txt","r")
    print(file.read())
except FileNotFoundError:
    #error handling code
    #print("Error occured!!!!!!!!")
    print("file not found")
finally:
    print("Program Ends")
    
