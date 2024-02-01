the_input = input()
list_of_numbers = the_input.split(' ')

for i in range(0, len(list_of_numbers)):
    list_of_numbers[i] = int(list_of_numbers[i]) * -1

print(list_of_numbers)
