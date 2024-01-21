number_of_rows = int(input())
total_sum = 0

for i in range(number_of_rows):
    the_character = input()
    total_sum += ord(the_character)

print(f"The sum equals: {total_sum}")