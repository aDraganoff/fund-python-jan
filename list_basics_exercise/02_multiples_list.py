factor = int(input())
count = int(input())
my_list = [factor]
for i in range(count-1):
    my_list.append(my_list[-1]+factor)
print(my_list)