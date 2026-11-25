# Task 3: Prime Number Analysis

try:
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
except ValueError:
    print("Invalid input. Please enter whole numbers.")
    raise SystemExit

if start > end:
    print("The starting number must not be greater than the ending number.")
    raise SystemExit

prime_numbers = []

for number in range(start, end + 1):
    if number < 2:
        continue

    is_prime = True

    # A prime number has no divisor other than 1 and itself.
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        prime_numbers.append(number)

if prime_numbers:
    print("Prime numbers:", *prime_numbers)
else:
    print("No prime numbers were found in this range.")

print("Total prime numbers:", len(prime_numbers))
print("Sum of prime numbers:", sum(prime_numbers))
