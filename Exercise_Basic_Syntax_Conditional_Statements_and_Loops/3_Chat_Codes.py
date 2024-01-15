command_count = int(input())

for i in range(command_count):
    command = int(input())
    if command == 88:
        print(f"Hello")
    elif command == 86:
        print(f"How are you?")
    elif command != 88 and command != 86 and command < 88:
        print(f"GREAT!")
    elif command > 88:
        print(f"Bye.")