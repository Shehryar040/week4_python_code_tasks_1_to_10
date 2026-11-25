# Task 9: Fibonacci Sequence and Sum

try:
    terms = int(input("How many Fibonacci terms do you want? "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    raise SystemExit

if terms < 1:
    print("The number of terms must be at least 1.")
    raise SystemExit

first = 0
second = 1
sequence = []
total = 0
even_count = 0
odd_count = 0

for _ in range(terms):
    current = first
    sequence.append(current)
    total += current

    if current % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    first, second = second, first + second

print("Fibonacci sequence:", *sequence)
print("Sum:", total)
print("Even terms:", even_count)
print("Odd terms:", odd_count)
