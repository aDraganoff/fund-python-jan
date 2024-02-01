def is_perfect_number(number):
    sum_of_devidors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_of_devidors += i
    if sum_of_devidors == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


numbers = int(input())
result = is_perfect_number(numbers)
print(result)
