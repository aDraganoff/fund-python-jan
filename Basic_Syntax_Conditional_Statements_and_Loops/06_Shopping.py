budget = int(input())
bill = 0
item = input()
complete = True
while item != "End":
    bill += int(item)
    if bill > budget:
        complete = False
        break
    item = input()
if complete:
    print(f"You bought everything needed.")
else:
    print(f"You went in overdraft!")
