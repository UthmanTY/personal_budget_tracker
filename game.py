import datetime
def add_transaction(transactions, type):
    description=input("Enter description: ")
    amount=float(input("Enter amount: "))
    date= datetime.date.today().isoformat()
    if type == "income":
        source=input("Enter income source: ")
        new_record = {
            "type": type,
            "description": description,
            "source": source,
            "amount": amount,
            "date": date
        }
    else:
        category=input("Enter expense category: ")
        new_record = {
            "type": type,
            "description": description,
            "category": category,
            "amount": amount,
            "date": date
        }
    transactions.append(new_record)
    print("Transaction added successfully")
