#Personal Finance App
expenses = []  #list of expenses in the form of dictionary

print("Welcome to the Expense Tracker App💰")

while True:
    print("Choose a number for any activity from the MENU:")
    print("1) Add Expense")
    print("2) View All Expenses")
    print("3) View Total Cost")
    print("4) Exit")
    
    choice = int(input("Enter a number: "))
    
    #Add Expense
    if(choice == 1):
        date = input("Enter the date of spending money: ")
        category = input("On which item(s) did you spend the money?: ")
        description = input("Add details of why you spent money on that item(s): ")
        amount = int(input("Enter the amount spent: "))
        
        expense = {
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : amount
        }
        expenses.append(expense)
        print("\nExpense is added SUCCESSFULLY!🥳")
        
        
    #View All Expenses
    elif (choice == 2):
        if(len(expenses) == 0):
            print("No expenses to show😕")
        else:
            print("Your expenses are as follows:")
            count = 1
            for eachcost in expenses:
                print(f"Expense number {count} -> {eachcost["date"]}, {eachcost["category"]},{eachcost["description"]},{eachcost["amount"]}")
                count += 1
                
    #View Total Cost
    elif (choice == 3):
        total = 0
        for eachcost in expenses:
            total = total + eachcost["amount"]
           
        print("\nTotal Cost is: ", total)
        
        
    #Exit
    elif (choice == 4):
        print("You have successfully exited from the app.✅")
        break
    else:
        print("Invalid choice❌\nTry again!🔄")
                           