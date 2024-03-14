def add_expenses(expenses,description,amount):
    expenses.append({"description" : description, "amount" : amount})
    print(f"Added expense : {description}, Amount = {amount}")
    
def get_total_expenses(expenses):
    sum = 0
    for expense in expenses:
        sum += expense["amount"]
    return sum

def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses) 

def show_budget_details(budget,expenses):
    print(f"Total Budget : {budget}")
    print("Expenses : ")
    for expense in expenses:
        print(f"- {expense['description']} : {expense['amount']}")
    print(f"Total Spent : {get_total_expenses(expenses)}")
    print(f"Remaining budget : {get_balance(budget,expenses)}")
    


def main():
    print("Welcome to the Budget Tracker App!")
    initial_budget = float(input("Please enter your initial budget :"))
    budget = initial_budget
    expenses = []
    
    while True:
        print("\nWhat would you like to do?")
        print("1.Add an expense")
        print("2.Show budget details")
        print("3.Exit")
        choice = input("Enter your choice (1/2/3) : ")
        
        if choice == "1":
            description = input("Enter expense description : ")
            amount = float(input("Enter expense amount : "))
            add_expenses(expenses,description,amount)
        elif choice == "2":
            show_budget_details(budget, expenses)
        elif choice == "3":
            print("Exiting Budget Tracker App.....Goodbye!")
            break
        else:
            print("Invalid choice, please choose again.")
            
        
if __name__ == "__main__":
    main()