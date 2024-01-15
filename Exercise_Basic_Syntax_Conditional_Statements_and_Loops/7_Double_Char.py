string = input()
while string != "End":
    if string != "SoftUni":
        for i in range(len(string)):
            print(f"{string[i]}", end="")
            print(f"{string[i]}", end="")
        print()
    elif string == "SoftUni":
        pass

    string = input()
