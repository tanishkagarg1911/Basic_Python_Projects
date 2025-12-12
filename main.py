# EXPENSE TRACKER
print("WELCOME TO EXPENSE TRACKER")

expenses = []

while True:
    print("MENU")
    print("1. ADD EXPENSE")
    print("2. VIEW ALL EXPENSE")
    print("3. VIEW TOTAL EXPENSE")
    print("4. EXIT")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        date=input("Enter your date:")
        category=input("Enter your category:")
        description=input("Enter your description:")
        amount=input("Enter your amount:")

        expense ={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }
        expenses.append(expense)
        print("done")

    elif choice == 2:
        if(len(expenses)==0):
            print("No expenses found")
        else:
            count=1
            for expense in expenses:
                print(f"EXPENSE NUMBER {count} ->{expense['date']},{expense['category']},{expense['description']},{expense['amount']}")
                count+=1

    elif choice == 3:
        total =0;
        for expense in expenses:
            total = total+expense['amount']

        print(f"Total Expenses : {total}")

    elif(choice == 4):
        print("Thankyou for using this system")
        break

    else:
        print("Invalid choice")



