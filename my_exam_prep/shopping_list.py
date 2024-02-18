my_shopping_list = input().split("!")
command = input()

while command != "Go Shopping!":
    action = command.split()[0]
    item = command.split()[1]
    if action == "Urgent":
        if item not in my_shopping_list:
            my_shopping_list.insert(0, item)
    elif action == "Unnecessary":
        if item in my_shopping_list:
            my_shopping_list.remove(item)
    elif action == "Correct":
        new_item_name = command.split()[2]
        if item in my_shopping_list:
            old_item_index = my_shopping_list.index(item)
            my_shopping_list[old_item_index] = new_item_name
    elif action == "Rearrange":
        if item in my_shopping_list:
            my_shopping_list.remove(item)
            my_shopping_list.append(item)
    command = input()

print(*my_shopping_list, sep=", ")
