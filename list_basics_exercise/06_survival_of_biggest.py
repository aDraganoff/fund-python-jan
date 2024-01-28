full_list = input().split(" ")
list_as_integers = []
remove_counter = int(input())
for integers in full_list:
    list_as_integers.append(int(integers))

for remove in range(remove_counter):
    list_as_integers.remove(min(list_as_integers))

print(*list_as_integers,sep=", ")
