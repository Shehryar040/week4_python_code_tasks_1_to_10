# Task 7: Pattern Generation

try:
    number = int(input("Enter a positive integer: "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    raise SystemExit

if number <= 0:
    print("The number must be positive.")
    raise SystemExit

print("\nIncreasing pattern:")
for row in range(1, number + 1):
    for value in range(1, row + 1):
        print(value, end="")
    print()

print("\nInverted pattern:")
for row in range(number, 0, -1):
    for value in range(1, row + 1):
        print(value, end="")
    print()

print("\nMultiplication table:")
for row in range(1, number + 1):
    for column in range(1, number + 1):
        print(f"{row * column:4}", end="")
    print()
