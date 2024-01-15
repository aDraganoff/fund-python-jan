budget = float(input())

flour = float(input())
eggs_pack = flour * 0.75
liter_milk = flour * 1.25
loaf_price = flour + eggs_pack + (liter_milk / 4)

#counters vars
current_bread_counter = 0
eggs_counter = 0

#money vars
total_price = 0
left_money = 0
while total_price < budget-loaf_price:
    current_bread_counter += 1
    total_price += loaf_price
    if current_bread_counter % 3 == 0:
        eggs_counter += 3
        eggs_counter = eggs_counter - (current_bread_counter - 2)
    else:
        eggs_counter += 3
left_money = budget - total_price

print(f"You made {current_bread_counter} loaves of Easter bread! Now you have {eggs_counter} eggs and {left_money:.2f}BGN left.")
