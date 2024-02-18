my_list = input().split(", ")

command = input()
while command != "Craft!":
    action, value = command.split(" - ")
    if action == "Collect":
        if value not in my_list:
            my_list.append(value)
    elif action == "Drop":
        if value in my_list:
            my_list.remove(value)
    elif action == "Combine Items":
        old_item, new_item = value.split(":")
        if old_item in my_list:
            old_item_index = my_list.index(old_item)
            my_list.insert(old_item_index+1, new_item)
    elif action == "Renew":
        if value in my_list:
            my_list.remove(value)
            my_list.append(value)

    command = input()

print(*my_list, sep=", ")
