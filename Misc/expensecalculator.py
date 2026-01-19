total = 0

for expense_number in range(4):
    expense_amount = float(input("Expense number " + str(expense_number + 1) + ": "))
    if expense_amount > 0:
        total += expense_amount
    else:
        print("Negative or zero expenses cannot be claimed, this input was ignored.")
    print("Your new total is:", total)

print("Your final expense total is:", total)