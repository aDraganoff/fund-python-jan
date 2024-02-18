def sum_full_order(my_list, discount_type):
    final_sum = 0
    taxes = 0
    price_with_taxes = 0
    if len(my_list) != 0:
        for index in range(0, len(my_list)):
            final_sum += my_list[index]
        if discount_type == "special":
            taxes = final_sum * 0.2
            price_with_taxes = (final_sum * 1.2) * 0.9
        elif discount_type == "regular":
            taxes = final_sum * 0.2
            price_with_taxes = final_sum * 1.2
    else:
        return "Invalid order!", 0, 0
    return final_sum, taxes, price_with_taxes


price_and_client = []
client_type = ""

while True:
    command = input()
    if command != "regular" and command != "special":
        if float(command) > 0:
            price_and_client.append(float(command))
        else:
            print(f"Invalid price!")
            continue
    else:
        client_type = command
        break
order_sum, tax, taxed_price = sum_full_order(price_and_client, client_type)
if order_sum != "Invalid order!" and order_sum != 0:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes:{order_sum: .2f}$")
    print(f"Taxes:{tax: .2f}$")
    print(f"-----------")
    print(f"Total price:{taxed_price: .2f}$")
else:
    print(f"Invalid order!")

