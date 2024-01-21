count_of_letters = int(input())

for first_dec in range(97, 97+count_of_letters):
    for second_dec in range(97, 97+count_of_letters):
        for third_dec in range(97, 97+count_of_letters):
            first_char = chr(first_dec)
            second_char = chr(second_dec)
            third_char = chr(third_dec)
            print(f"{first_char}{second_char}{third_char}")

