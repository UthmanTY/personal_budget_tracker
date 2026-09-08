
def get_summary(transactions):
  total_expense = 0
  total_income = 250000.00
  #amount = transactions.get("amount")
  #iterate through the list of expenses
  for data in transactions:
    #iterate through each dictionary of expenses to get amount of each expense
    for amount in data.values():
      #if the value of the amount is a number, add it to total expense and return total
      if isinstance(amount, float) and not isinstance(amount, str):
        total_expense += amount
        #print(f"Total amount: {total_expense}")
    net_balance = total_income - total_expense
    #print(net_total)
    return net_balance
