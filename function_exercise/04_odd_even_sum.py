def sum_odd_even(a):
    even_sum = 0
    odd_sum = 0
    number_to_string = str(a)
    for char in number_to_string:
        digit = int(char)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    return odd_sum, even_sum


number = int(input())
printer = sum_odd_even(number)

print(f"Odd sum = {printer[0]}, Even sum = {printer[1]}")
