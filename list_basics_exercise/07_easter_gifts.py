gifts_list = input().split()
no_money = True
while no_money:
    command = input().split()
    if command[0] == "OutOfStock":
        gifts_list = list(map(lambda x: x.replace(command[1], "None"), gifts_list))
    elif command[0] == "Required":
        if 0 <= int(command[2]) < len(gifts_list) :
            gifts_list[int(command[2])] = command[1]
        else:
            continue
    elif command[0] == "JustInCase":
        gifts_list[-1] = command[1]
    elif command[0] == "No":
        no_money = False

for items in gifts_list:
    if items != "None":
        print(items, end=" ")
