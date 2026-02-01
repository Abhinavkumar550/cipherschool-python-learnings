print("------Welcome to Expense Calculator------")
file_name="expenses_data.txt"
#show menu
#add expense
#view expense
#total expense
#exit
#user selects one option
#fucntion runs
#save data
#repeat
expenses=[]
def load_data():
    global expenses
    try:
        file=open(file_name,"r")
        lines=file.readlines()
        for line in file:
            amount, category, description = line.strip().split(",")
            expenses.append({"amount": int(amount),"category": category,"description": description})
        file.close()
    except:
        pass
def save_expense():
    file=open(file_name,"w")
    for i in file:
        a={amount,category,description}
        c=file.write(a)
def add_expense():
    amount=int(input("Enter the amount:"))
    category=input("Enter the category: "))
    description=input("Enter the description: ")
    expense.append(amount,category,description)
    
    
    
    
    
        
