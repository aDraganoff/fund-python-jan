def manipulate_targets(list_of_targets):
    shoot_counter = 0
    while True:
        command = input()
        current_target = 0
        if command != "End":
            if int(command) <= len(list_of_targets)-1:
                if list_of_targets[int(command)] != -1:
                    shoot_counter += 1
                    current_target = list_of_targets[int(command)]
                    list_of_targets[int(command)] = -1
                    for target in range(0, len(list_of_targets)):
                        if list_of_targets[target] != -1:
                            if list_of_targets[target] > current_target:
                                list_of_targets[target] -= current_target
                            else:
                                list_of_targets[target] += current_target
                        else:
                            continue
                    list_of_targets[int(command)] = -1
                else:
                    continue
            else:
                continue
        else:
            break

    return list_of_targets, shoot_counter


targets = input().split()
targets_to_int = list(map(int, targets))
shooted_targets, shoots = manipulate_targets(targets_to_int)

print(f"Shot targets: {shoots} -> ", end="")
print(" ".join(map(str, shooted_targets)))

