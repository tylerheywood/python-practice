transactions = []
balance = 0
transaction_amount = float(input("Welcome to TyNance, What is the value of this transaction? (enter 0 to end this process) "))

#calculate balance function
def calculate_balance(transactions):
    balance = 0
    for transaction in transactions:
        balance += transaction
    return balance

def recall_transaction(transactions, transaction_number):
    if 1 <= transaction_number <= len(transactions):
        print(f"Transaction # {transaction_number}: {transactions[transaction_number - 1]}")
    else:
        print("This transaction number does not exist!")

def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

while transaction_amount != 0:
    transactions.append(transaction_amount)
    transaction_amount = get_float("What is the value of this transaction? (enter 0 to end this process) ")


balance = calculate_balance(transactions)

print("Your final balance is: ", balance)
transaction_number = int(input("Do you want to view any transactions? (enter 0 to end this process) "))
while transaction_number != 0:
    recall_transaction(transactions, transaction_number)
    transaction_number = int(input("Do you want to view any transactions? (enter 0 to end this process) "))


print("Thank you for using TyNance.")

