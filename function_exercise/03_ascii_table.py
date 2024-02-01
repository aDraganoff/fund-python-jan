def ascii_symbols(a, b):
    symbols = []
    for _ in range(ord(a) + 1, ord(b)):
        symbols.append(chr(_))
    return symbols


first_char = input()
second_char = input()
chars = ascii_symbols(first_char, second_char)
for symb in chars:
    print(symb, end=" ")

