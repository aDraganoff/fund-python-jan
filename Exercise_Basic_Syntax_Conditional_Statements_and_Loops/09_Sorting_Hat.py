student_name = input()

while student_name != "Welcome!":
    if student_name != "Voldemort":
        if len(student_name) < 5:
            print(f"{student_name} goes to Gryffindor.")
        elif len(student_name) == 5:
            print(f"{student_name} goes to Slytherin.")
        elif len(student_name) == 6:
            print(f"{student_name} goes to Ravenclaw.")
        elif len(student_name) > 6:
            print(f"{student_name} goes to Hufflepuff.")
    else:
        print(f"You must not speak of that name!")
        break
    student_name = input()
if student_name != "Voldemort":
    print(f"Welcome to Hogwarts.")
else:
    pass
