import datetime

def add_transaction(transactions, type):
    # Handle an income transaction
    if type == "income":
        income_source = input("What is your income source? ")
        description = input("What is the description? ")
        amount = float(input("Enter amount: "))
        date = datetime.date.today().isoformat()

        # Store the income details in a dictionary
        income = {
            "type": type,
            "income_source": income_source,
            "description": description,
            "amount": amount,
            "date": date
        }

        # Add the new transaction dictionary to the transactions list
        transactions.append(income)
        print("Income transaction added successfully.")

    # Handle an expense transaction
    elif type == "expense":
        expense_category = input("What is the expense category? ")
        description = input("What is the description? ")
        amount = float(input("Enter amount: "))
        date = datetime.date.today().isoformat()

        # Store the expense details in a dictionary
        expense = {
            "type": type,
            "expense_category": expense_category,
            "description": description,
            "amount": amount,
            "date": date
        }

        # Add the new transaction dictionary to the transactions list
        transactions.append(expense)
        print("Expense transaction added successfully.")

    # Handle an unexpected transaction type
    else:
        print("Invalid transaction type!")


def view_all(transactions):
    # Check whether there are any transactions to display
    if not transactions:
        print("The transactions list is empty.")
        return

    # Display the column headings once before displaying the transactions
    print(f"{'Type':<10} {'Source/Category':<20} {'Description':<20} {'Amount':>12} {'Date':<12}")

    # Loop through every transaction in the list
    for transaction in transactions:

        # Get the appropriate source/category depending on the transaction type
        if transaction["type"] == "income":
            source_or_category = transaction["income_source"]
        elif transaction["type"] == "expense":
            source_or_category = transaction["expense_category"]
        else:
            # Skip a transaction if it has an unexpected type
            print("Invalid transaction")
            continue

        # Display the details of the current transaction
        # Amount is right-aligned, comma-separated, and shown to 2 decimal places
        print(f'{transaction["type"]:<10} {source_or_category:<20} {transaction["description"]:<20} {transaction["amount"]:>12,.2f} {transaction["date"]:<12}')


def get_summary(transactions):
  total_expense = sum(t["amount"] for t in transactions if t["type"] == "expense")
  total_income = sum(t["amount"] for t in transactions if t["type"] == "income")
#   amount = transactions.get("amount")
  #iterate through the list of expenses
    #iterate through each dictionary of expenses to get amount of each expense

      #if the value of the amount is a number, add it to total expense
        #print(f"Total amount: {total_expense}")
        #return total_expense
    #calculate net balance remaining by deducting total_expense from total_income
  net_balance = total_income - total_expense
    #print(net_balance)
  print("\n📊 FINANCIAL SUMMARY")
  print("--------------------------")
  print(f"{'Total Income:':<20} {total_income:>10}")
  print(f"{'Total Expenses:':<20} {total_expense:>10}")
  print(f"{'Net Balance:':<20} {net_balance:>10}")


def view_by_category(transactions):
 

    categories = {}

    for t in transactions:
        if t["type"] == "expense":
            category = t["expense_category"]
            amount = t["amount"]
            categories[category] = categories.get(category, 0) + amount


    if not categories:
        print("\nNo expense records found.")
        return

    # Compute total expenses across all categories
    total_expenses = sum(categories.values())

    # Print formatted results
    print("\n📁 SPENDING BY CATEGORY")
    print("--------------------------")
    
    for category, amount in categories.items():
        # Calculate percentage share
        percentage = (amount / total_expenses) * 100 if total_expenses > 0 else 0
        
        # Print with aligned formatting and currency symbol
        print(f"{category:<15} ₦ {amount:>10,.2f}  ({percentage:>5.1f}%)")

