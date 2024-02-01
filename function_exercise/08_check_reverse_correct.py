def check_palindrome(number):
    if number == number[::-1]:
        return True
    return False


list_of_numbers = input().split(", ")

for number in list_of_numbers:
    if check_palindrome(number):
        print("True")
    else:
        print("False")
