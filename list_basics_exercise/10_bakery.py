events = input().split("|")
total_coins = 100
total_energy = 100
bakery_is_open = True
for event in events:
    event_items = event.split("-")
    type_of_event = event_items[0]
    value_of_event = int(event_items[1])

