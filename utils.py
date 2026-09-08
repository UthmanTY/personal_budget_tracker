import datetime

def add_transaction(transactions, type):
    if type == "income":
        income_source = input("What is your income source? ")
        description = input("What is the description? ")
        amount = float(input("Enter amount: "))
        date = datetime.date.today().isoformat()

        income = {
            "type":type, 
            "income_source":income_source,
            "description":description, 
            "amount": amount, 
            "date":date
                }
        transactions.append(income)
        print("Income transaction added successfully.")
    elif type == "expense":
        expense_category = input("What is the expense category? ")
        description = input("What is the description? ")
        amount = float(input("Enter amount: "))
        date = datetime.date.today().isoformat()

        expense = {
            "type":type, 
            "expense_category":expense_category,
            "description":description, 
            "amount": amount, 
            "date":date
        }
        transactions.append(expense)
        print("Expense transaction added successfully.")
    else:
        print("Invalid transaction type!")

def view_all(transactions):
    if not transactions:
        print("The transactions list is empty.") 
        return

    print(f"{'Type':<10} {'Source/Category':<20} {'Description':<20} {'Amount':>12} {'Date':<12}")
    for transaction in transactions:
        if transaction["type"] == "income":
            source_or_category = transaction["income_source"]
        elif transaction["type"] == "expense":
            source_or_category = transaction["expense_category"]
        else:
            print("Invalid transaction")
            continue

        print(f'{transaction["type"]:<10} {source_or_category:<20} {transaction["description"]:<20} {transaction["amount"]:>12,.2f} {transaction["date"]:<12}')
