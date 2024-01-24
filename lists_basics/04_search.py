line_numbers = int(input())
word = input()
my_list = []
for i in range(line_numbers):
    my_string = input()
    my_list.append(my_string)

print(my_list)
for n in range(len(my_list)-1, -1 ,-1):
    element = my_list[n]
    if word not in element:
        my_list.remove(element)
print(my_list)