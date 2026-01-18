prices = []
new_item = input("Please enter all prices, one by one: ")

while new_item != "done":
    converted_price = float(new_item)
    prices.append(converted_price)
    new_item = input("Please enter all prices, one by one: ")

total = sum(prices)


print("Items: ", len(prices))
print("Total: ", total)
print("Average: ", round(total / len(prices),2))




