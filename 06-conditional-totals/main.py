count = 0
total = 0
even_total = 0
odd_total = 0

number = int(input("Enter a number: "))

while number != 0:
    total += number
    count += 1
    if number % 2 == 0:
        even_total += number
    else:
        odd_total += number

    number = int(input("Enter a number: "))

print(f"The count is: {count}")
print(f"The total is: {total}")
print(f"The even total is: {even_total}")
print(f"The odd total is: {odd_total}")