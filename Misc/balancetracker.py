transaction_amount = int(input("What is the value of this transaction? (enter 0 to end this process) "))
balance = 0

while transaction_amount != 0:
    balance = balance + transaction_amount
    print("Your new total is: ", balance)
    transaction_amount = int(input("What is the value of this transaction? (enter 0 to end this process) "))

print("Your final balance is: ", balance)

