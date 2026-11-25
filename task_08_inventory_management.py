# Task 8: Inventory Management System

stock = 100
total_sold = 0

print(f"Starting stock: {stock} units")

while stock > 0:
    try:
        quantity = int(input("Enter quantity sold (-1 to stop): "))
    except ValueError:
        print("Invalid input. Enter a whole number.")
        continue

    if quantity == -1:
        break

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        continue

    if quantity > stock:
        print(f"Sale rejected. Only {stock} units are available.")
        continue

    stock -= quantity
    total_sold += quantity
    print(f"Sale accepted. Remaining stock: {stock} units")

print(f"\nTotal units sold: {total_sold}")
print(f"Remaining stock: {stock}")
