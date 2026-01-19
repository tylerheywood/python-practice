income = int(input("Enter your income: "))
expenses = int(input("Enter your expenses: "))

savings = income - expenses

if savings < 0:
    print("We're not saving any money!")
elif savings == 0:
    print("You're breaking even!")
else:
    print("Monthly Savings:", savings)
