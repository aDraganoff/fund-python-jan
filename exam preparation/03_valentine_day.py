def cupidon(hood_list):
    last_position = 0
    while True:
        cupidon_command = input().split()
        if cupidon_command != "Love!":
            steps = int(cupidon_command[1]) + last_position
            if steps <= len(hood_list)-1 :

            else:
                steps = steps % len(hood_list)-1

        else:
            pass


count_of_hearts_as_string = input().split("@")
count_of_hearts = list(map(int, count_of_hearts_as_string))

