people = int(input())
capacity = int(input())
courses_counter = 0
while people > 0:
    people -= capacity
    courses_counter += 1

print(courses_counter)