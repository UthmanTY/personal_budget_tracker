import sys
from utils import add_transaction, view_all, get_summary, view_by_category

transactions = []
type1 = str.lower("income")
type2 = str.lower("expense")

while True:
    print("==== BUDGET TRACKER ====")
    print("[1] Add Income  [2] Add Expense  [3] View All  [4] Summary  [5] By Category  [6] Exit")

    user_input = input("> ")

    if user_input == "1":
        add_transaction(transactions, type1)
    elif user_input == "2":
        add_transaction(transactions, type2)
    elif user_input == "3":
        view_all(transactions)
    elif user_input == "4":
        get_summary(transactions)
    elif user_input == "5":
        view_by_category(transactions)
    elif user_input == "6":
        sys.exit()
    else:
        print("Please enter a valid number from the provided options")
        continue