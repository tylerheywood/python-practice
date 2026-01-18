user_input = input("Please enter a number: ")
n = int(user_input)
factor_1 = 3
factor_2 = 5
total = 0

for num in range(1, n + 1):
    if num % factor_1 == 0:
        total = total + num
    elif num % factor_2 == 0:
        total = total + num

print("Sum: " + str(total))


