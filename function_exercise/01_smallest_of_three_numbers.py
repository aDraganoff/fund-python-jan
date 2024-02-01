def check_values(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    return numbers[0]


first_number = int(input())
second_number = int(input())
third_number = int(input())

result = check_values(first_number, second_number, third_number)
print(result)
