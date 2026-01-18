'''
running analysis of total, count and average

constraints:
- no lists
- no sum() or len()
'''

total = 0
count = 0

number = int(input("Enter a number: "))

while number !=0:
    total += number
    count += 1
    number = int(input("Enter a number: "))


average = total / count

print(f"Count: {count}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
