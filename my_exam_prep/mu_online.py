rooms = input().split("|")
health = 100
bitcoins = 0
alive = True
for i in range(len(rooms)):
    command, value = rooms[i].split()
    if command != "chest" and command != "potion":
        health -= int(value)
        if health <= 0:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {i+1}")
            alive = False
            break
        else:
            print(f"You slayed {command}.")
    elif command == "potion":
        if health + int(value) > 100:
            diff = 100 - health
            health = 100
            print(f"You healed for {diff} hp.")
            print(f"Current health: {health} hp.")
        else:
            health += int(value)
            print(f"You healed for {value} hp.")
            print(f"Current health: {health} hp.")
    elif command == "chest":
        print(f"You found {value} bitcoins.")
        bitcoins += int(value)
if alive:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")

