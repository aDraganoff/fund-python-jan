memory_list = input().split()
command = input()
moves_counter = 0
correct_answers = 0
is_win = False
while command != "end":
    moves_counter += 1
    first_index = int(command.split()[0])
    second_index = int(command.split()[1])
    if first_index == second_index or first_index < 0 or second_index < 0 or first_index > len(memory_list) - 1 \
            or second_index > len(memory_list) - 1:
        memory_list_middle = int(len(memory_list) / 2)
        print(f"Invalid input! Adding additional elements to the board")
        memory_list.insert(memory_list_middle, "-" + str(moves_counter) + "a")
        memory_list.insert(memory_list_middle, "-" + str(moves_counter) + "a")
    elif memory_list[first_index] != memory_list[second_index]:
        print(f"Try again!")
    elif memory_list[first_index] == memory_list[second_index]:
        print(f"Congrats! You have found matching elements - {memory_list[first_index]}!")
        if first_index < second_index:
            memory_list.pop(second_index)
            memory_list.pop(first_index)
        else:
            memory_list.pop(first_index)
            memory_list.pop(second_index)
    if len(memory_list) <= 0:
        print(f"You have won in {moves_counter} turns!")
        is_win = True
        moves_counter -= 1
        break
    command = input()

if not is_win:
    print(f"Sorry you lose :(")
    print(*memory_list, sep=" ")
