number_of_strings = int(input())


for i in range(number_of_strings):
    string = input()
    notPure = False
    for j in range(len(string)):
        if string[j] == "," or string[j] == "." or string[j] == "_":
            notPure = True
            continue
        else:
            pass
    if notPure:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")
