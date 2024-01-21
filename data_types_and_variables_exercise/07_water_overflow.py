count_of_commands = int(input())
tank_liters = 0

for i in range(count_of_commands):
    add_litters = int(input())
    if tank_liters + add_litters <= 255:
        tank_liters += add_litters
    else:
        print(f"Insufficient capacity!")
print(tank_liters)
