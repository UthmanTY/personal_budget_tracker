
def get_summary(transactions):
  total_expense = 0
  total_income = 250000.00
  #amount = transactions.get("amount")
  #iterate through the list of expenses
  for data in transactions:
    #iterate through each dictionary of expenses to get amount of each expense
    for amount in data.values():
      #if the value of the amount is a number, add it to total expense
      if isinstance(amount, float) and not isinstance(amount, str):
        total_expense += amount
        #print(f"Total amount: {total_expense}")
        #return total_expense
    #calculate net balance remaining by deducting total_expense from total_income
    net_balance = total_income - total_expense
    #print(net_total)
    return net_balance


def view_by_category(transactions):
 

    categories = {}

    for t in transactions:
        if t["type"] == "expense":
            category = t["category"]
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

