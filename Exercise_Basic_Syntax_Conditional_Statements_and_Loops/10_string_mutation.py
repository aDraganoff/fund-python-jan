first_string = input()
second_string = input()
last_transform = first_string

for char_index in range(len(first_string)):
    left_side = second_string[:char_index+1]
    right_side = first_string[char_index+1:]
    new_string = left_side + right_side
    if new_string != last_transform:
        print(new_string)
        last_transform = new_string
