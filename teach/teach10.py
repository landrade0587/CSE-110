print("Enter the names and prices of the products in the store a list of products in a shopping cart (type: quit when done)")

name = []
price = []

names = None

# Build the lists
while name != "quit":
    name = input("What item would you like to add? ")

    if name != "quit":
       price = float(input(f"What is the price of {name}? "))

      names.append(name)
      prices.append(price)

# Display all of the accounts with their balances
# Compute the total at the same time.
total = 0

print("\nList Information:")
for i in range(len(names)):
    print(f"{i}. {names[i]} - ${price[i]:.2f}")

    total += price[i]

average = total / len(price)

print()
print(f"Total: ${total:.2f}")
print(f"Average: ${average:.2f}")

# Stretch Challenges:

# Find the highest balance:
highest_name = None
highest_price = -1

for i in range(len(names)):
    name = names[i]
    price = price[i]

    if price > highest_price:
        # We have a new highest!
        highest_price = price
        highest_name = name

print(f"Highest price: {highest_name} - ${highest_price:.2f}")

change_account = "yes"

while change_account == "yes":
    change_account = input("\nDo you want to update an account? ")

    if change_account == "yes":
        index = int(input("What account index do you want to update? "))
        new_amount = float(input("What is the new amount? "))

        price[index] = new_amount
    
    # Now print the balances
    print("\nAccount Information:")
    for i in range(len(names)):
        print(f"{i}. {names[i]} - ${price[i]:.2f}")