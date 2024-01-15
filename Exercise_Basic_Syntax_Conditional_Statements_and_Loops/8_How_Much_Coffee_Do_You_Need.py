tasks = input()
coffee_counter = 0
while tasks != "END":
    if tasks.isupper():
        if tasks == "CODING" or tasks == "DOG" or tasks == "CAT" or tasks == "MOVIE":
            coffee_counter += 2
        else:
            pass
    elif tasks.islower():
        if tasks == "coding" or tasks == "dog" or tasks == "cat" or tasks == "movie":
            coffee_counter += 1
        else:
            pass

    tasks = input()
if coffee_counter > 5:
    print(f"You need extra sleep")
else:
    print(coffee_counter)
