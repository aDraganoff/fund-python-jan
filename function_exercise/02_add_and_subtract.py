def sum_numbers(a, b):
    result = a+b
    return result


def subtract(num1, num2):
    result = num1 - num2
    return result


def add_and_subtract():
    a = int(input())
    b = int(input())
    c = int(input())
    result = subtract(sum_numbers(a, b), c)
    return result


res = add_and_subtract()
print(res)
