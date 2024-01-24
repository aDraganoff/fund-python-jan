n = int(input())
list_of_numbers = []
filtered_numbers = []

for i in range(n):
    number = int(input())
    list_of_numbers.append(number)

command = input()

if command == "even":
    for _ in range(len(list_of_numbers)):
        if list_of_numbers[_] % 2 == 0:
            filtered_numbers.append(list_of_numbers[_])
elif command == "odd":
    for _ in range(len(list_of_numbers)):
        if list_of_numbers[_] % 2 != 0:
            filtered_numbers.append(list_of_numbers[_])
elif command == "positive":
    for _ in range(len(list_of_numbers)):
        if list_of_numbers[_] >= 0:
            filtered_numbers.append(list_of_numbers[_])
elif command == "negative":
    for _ in range(len(list_of_numbers)):
        if list_of_numbers[_] < 0:
            filtered_numbers.append(list_of_numbers[_])
print(filtered_numbers)
