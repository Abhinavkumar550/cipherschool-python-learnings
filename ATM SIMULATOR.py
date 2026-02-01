print("-----welcome to ATM Simulator-----")
file_name="atm.txt"
#balance is a global variable that stores money 
balance=1000
#pin is a global variable that stores pin 
pin="1234"
#load data
def load_data():
    #global keywords allows us to modify outside variable
    global balance,pin
    try:
        file=open(file_name,"r")
        #reading whole lines 
        lines=file.readlines()
        file.close()
        #removing starting and ending spaces using strip()
        pin=lines[0].strip()
        balance=int(lines[1].strip())
    except:
        #if file doesn't exist then pass will work and do nothing
        #program will use default balance and pin
        pass
#check balance
def check_balance():
    print("Your balance is :",balance)
#Save data
def save_data():
    #opening a file in write mode and writing pin and balance 
    file=open(file_name,"w")
    file.write(pin+"\n")
    #we are converting balance into string and writing into file 
    file.write(str(balance))
    file.close()
def deposit_money():
    #global allows us to change original balance
    global balance
    try:
        amount=int(input("Enter amount to deposit: "))
        balance=balance+amount
        save_data()
        print("Money deposited successfully")
    except:
        print("Please enter number only")
def withdraw_money():
    global balance
    try:
        amount=int(input("Enter the money to be withdrawn: "))
        if(amount>balance):
            print("You don't have enough balance")
        else:
            balance=balance-amount
            save_data()
            print("Please collect your money !!!")
            file.close()
    except:
        print("Please enter number only")
def change_pin():
    global pin
    #ask user old pin
    old_pin=input("Enter the old pin: ")
    #checking if old pin matches
    if old_pin==pin:
        new_pin=input("Enter your new pin")
        pin=new_pin
        save_data()
        print("Pin changed successfully")
    else:
        print("Incorrect Pin")
        return

def main():
    #load data when program starts
    load_data()
    #ask user to enter pin
    user_pin=input("enter the pin:")
    if user_pin!=pin:
        print("Incorrect pin")
        return
    while True:
        print("\n------ATM MENU------")
        print("1.Check Balance")
        print("2.Deposit Money")
        print("3.Withdraw Money")
        print("4.Change Pin")
        print("5.Exit")
        choice=input("Enter your choice:")
        if choice=="1":
            check_balance()
        elif choice=="2":
            deposit_money()
        elif choice=="3":
            withdraw_money()
        elif choice=="4":
            change_pin()
        elif choice=="5":
            print("Thank you")
            break
        else:
            print("Invalid choice")
main()
    
            
    
    
    
        

