orders = int(input())
total = 0
for i in range(0, orders):
    capsule_price = float(input())
    days = int(input())
    capsule_per_day = int(input())
    if capsule_price < 0.01 or capsule_price > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsule_per_day < 1 or capsule_per_day > 2000:
        continue
    money = capsule_price * (days * capsule_per_day)
    total += money
    print(f"The price for the coffee is: ${money:.2f}")

print(f"Total: ${total:.2f}")
