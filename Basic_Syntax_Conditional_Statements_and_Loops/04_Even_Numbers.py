n = int(input())

for i in range(n):
    number = int(input())
    if number % 2 == 0:
        pass
    else:
        print(f"{number} is odd!")
        break
else:
    print(f"All numbers are even.")
