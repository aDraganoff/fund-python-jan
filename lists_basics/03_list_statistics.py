positive_list = []
negative_list = []
count_of_numbers = int(input())

for number in range(count_of_numbers):
    the_number = int(input())
    if the_number >= 0:
        positive_list.append(the_number)
    else:
        negative_list.append(the_number)
sum = sum(negative_list)
print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {sum}")
