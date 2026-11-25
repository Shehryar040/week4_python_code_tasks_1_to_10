

marks = []

for student in range(1, 11):
    while True:
        try:
            mark = float(input(f"Enter marks for student {student} (0-100): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100. Try again.")
            continue

        marks.append(mark)
        break

print("\nStudent Results")
for student, mark in enumerate(marks, start=1):
    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"Student {student}: {mark:g} marks - Grade {grade}")

passed = 0
failed = 0
for mark in marks:
    if mark >= 50:
        passed += 1
    else:
        failed += 1

highest_mark = max(marks)
average = sum(marks) / len(marks)

print(f"\nPassed students: {passed}")
print(f"Failed students: {failed}")
print(f"Highest mark: {highest_mark:g}")
print(f"Class average: {average:.2f}")
