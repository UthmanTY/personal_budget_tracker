def add_transaction(transactions, type):
    description=input("Enter description: ")
    amount=float(input("Enter amount: "))
    if type == "income":
        source=input("Enter income source: ")
        new_record = {
            "type": type,
            "description": description,
            "source": source,
            "amount": amount,
        }
    else:
        category=input("Enter expense category: ")
        new_record = {
            "type": type,
            "description": description,
            "category": category,
            "amount": amount,
        }
    transactions.append(new_record)
    print("Transaction added successfully")
