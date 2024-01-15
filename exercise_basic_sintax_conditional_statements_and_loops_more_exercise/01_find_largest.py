number = input()
list_of_digits = [123423, 234525 , 234234 ,23423 ]
for i in range(0, len(number)):
    digit = int(number[i])
    list_of_digits.insert(i, digit)

list_of_digits.sort()
for j in range(len(number)-1, -1, -1):
    print(f"{list_of_digits[j]}", end="")

print()


