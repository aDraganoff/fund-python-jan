students = int(input())
total_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
max_attendance = 0

for students in range(students):
    current_attendances = int(input())
    current_bonus = current_attendances / total_lectures * (5 + additional_bonus)
    if current_bonus > max_bonus:
        max_bonus = current_bonus
        max_attendance = current_attendances

print(f"Max Bonus: {max_bonus:.0f}.")
print(f"The student has attended {max_attendance} lectures.")
