quantity = int(input())
days_to_christmas = int(input())

#items_price
ornamentset_price = 2
treeskrit_price = 5
treegarlant_price = 3
treelighters_price = 15

#item_spirit
ornamentset_spirit = 5
treeskirt_spirit = 3
treegarlant_spirit = 10
treelighters_spirit = 17

#counters
spirit = 0
money = 0

for day in range(1, days_to_christmas+1):
    if day % 11 == 0:
        quantity = quantity + 2
    if day % 2 == 0:
        money = money + (ornamentset_price * quantity)
        spirit += 5
    if day % 3 == 0:
        money = money + (treeskrit_price * quantity + treegarlant_price * quantity)
        spirit = spirit + (treeskirt_spirit + treegarlant_spirit)
    if day % 5 == 0:
        money = money + (treelighters_price * quantity)
        spirit = spirit + 17
        if day % 3 == 0:
            spirit += 30
    else:
        pass
    if day % 10 == 0:
        money = money + (treeskrit_price +
                         treelighters_price +
                         treegarlant_price)
        spirit = spirit - 20
if days_to_christmas % 10 == 0:
    spirit = spirit - 30


print(f"Total cost: {money}")
print(f"Total spirit: {spirit}")
