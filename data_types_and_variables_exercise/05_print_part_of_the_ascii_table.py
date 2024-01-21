start_number = int(input())
stop_number = int(input())

for chars in range(start_number, stop_number+1):
    the_char = chr(chars)
    print(f"{the_char}", end=" ")
