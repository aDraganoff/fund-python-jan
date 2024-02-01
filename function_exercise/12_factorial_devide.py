def calculate_factoriel(number):
    factoriel = number
    for i in range(number-1, 0, -1):
        factoriel = factoriel * i
    return factoriel


first_number = int(input())
second_number = int(input())
first_facturiel = calculate_factoriel(first_number)
second_facturiel = calculate_factoriel(second_number)
result = first_facturiel / second_facturiel
print(f"{result:.2f}")