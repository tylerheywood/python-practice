'''
🎯 Goal

Write a program that reads a stream of integers from the user and, when they finish, prints:

how many numbers were entered

the smallest number

the largest number

This is the first challenge where you must handle a “first value sets the baseline” pattern properly.

📥 Inputs

The user enters one integer at a time

Input ends when the user enters 0

Numbers can be positive or negative

0 is only the stop signal (don’t count it)

Assume at least one non-zero number will be entered.

⚠️ Constraints

❌ Do NOT use lists/tuples/sets/dicts

❌ Do NOT use min() or max()

❌ Do NOT use break

❌ No libraries

✅ Use a while loop

✅ Convert input to int immediately

✅ Must correctly initialise min_value and max_value based on the first non-zero input
'''

number = int(input("Enter a number: "))


count = 0
highest = number
lowest = number

while number != 0:
    count += 1
    if number > highest:
        highest = number
    if number < lowest:
        lowest = number

    number = int(input("Enter a number: "))

print(f"Count: {count}")
print(f"Min: {lowest}")
print(f"Max: {highest}")