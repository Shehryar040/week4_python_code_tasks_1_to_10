# Task 10: Menu-Driven Number Analysis System

even_count = 0
odd_count = 0
count = 0
largest = None
total = 0

print("Enter integers to analyze. Enter 0 to finish.")

while True:
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        continue

    if number == 0:
        break

    if number < 0:
        print("Negative number ignored.")
        continue

    count += 1
    total += number

    if number % 2 == 0:
        even_count += 1
        print(f"{number} is even.")
    else:
        odd_count += 1
        print(f"{number} is odd.")

    if largest is None or number > largest:
        largest = number

if count == 0:
    print("No positive numbers were entered, so an average cannot be calculated.")
else:
    average = total / count
    print(f"\nEven numbers: {even_count}")
    print(f"Odd numbers: {odd_count}")
    print(f"Largest positive number: {largest}")
    print(f"Sum of positive numbers: {total}")
    print(f"Average of positive numbers: {average:.2f}")
