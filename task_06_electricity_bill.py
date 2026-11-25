# Task 6: Electricity Bill Calculator

def calculate_bill(units):
    """Return the bill using progressive unit rates."""
    if units <= 100:
        return units * 10
    elif units <= 200:
        return (100 * 10) + ((units - 100) * 15)
    elif units <= 300:
        return (100 * 10) + (100 * 15) + ((units - 200) * 20)
    else:
        return (100 * 10) + (100 * 15) + (100 * 20) + ((units - 300) * 25)


total_revenue = 0
customer_count = 0

while True:
    try:
        units = int(input("Enter units consumed (-1 to stop): "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        continue

    if units == -1:
        break

    if units < 0:
        print("Unit consumption cannot be negative. Try again.")
        continue

    bill = calculate_bill(units)
    customer_count += 1
    total_revenue += bill
    print(f"Customer {customer_count} bill: Rs. {bill:,.2f}")

print(f"\nCustomers processed: {customer_count}")
print(f"Total revenue collected: Rs. {total_revenue:,.2f}")
