user_input = input("Enter a number: ")
n = int(user_input)

evens = 0
odds = 0


for num in range(1, n+1):
    if num % 2 == 0:
        evens = evens + 1
    else:
        odds = odds + 1


print("Evens:", evens)
print("Odds:", odds)
print("Total:", evens + odds)