
def get_summary(transactions):
  total_expense = 0
  #amount = transactions.get("amount")
  #iterate through the list of expenses
  for data in transactions:
    #iterate through each dictionary of expenses to get amount of each expense
    for amount in data.values():
      #if the value of the amount is a number, add it to total expense and return total
      if isinstance(amount, float) and not isinstance(amount, str):
        total_expense += amount
        #print(f"Total amount: {total_expense}")
        return total_expense

  
# text = get_summary([{
#     "type": "expense",       # or "income"
#     "category": "Food",
#     "description": "Lunch at work",
#     "amount": 1500.00,       # in your local currency
#     "date": "2024-01-15"     # added later using datetime module
# },{
#     "type": "expense",       # or "income"
#     "category": "Food",
#     "description": "Lunch at work",
#     "amount": 2500.00,       # in your local currency
#     "date": "2024-01-15"     # added later using datetime module
# },{
#     "type": "expense",       # or "income"
#     "category": "Food",
#     "description": "Lunch at work",
#     "amount": 100.00,       # in your local currency
#     "date": "2024-01-15"     # added later using datetime module
# }])


