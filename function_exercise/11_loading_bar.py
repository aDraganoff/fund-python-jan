def loading_bar(level):
    level_bar = int(level / 10)
    if level_bar == 0:
        print(f"{level}% [..........]")
        print(f"Still loading...")
    elif level_bar == 1:
        print(f"{level}% [%.........]")
        print(f"Still loading...")
    elif level_bar == 2:
        print(f"{level}% [%%........]")
        print(f"Still loading...")
    elif level_bar == 3:
        print(f"{level}% [%%%.......]")
        print(f"Still loading...")
    elif level_bar == 4:
        print(f"{level}% [%%%%......]")
        print(f"Still loading...")
    elif level_bar == 5:
        print(f"{level}% [%%%%%.....]")
        print(f"Still loading...")
    elif level_bar == 6:
        print(f"{level}% [%%%%%%....]")
        print(f"Still loading...")
    elif level_bar == 7:
        print(f"{level}% [%%%%%%%...]")
        print(f"Still loading...")
    elif level_bar == 8:
        print(f"{level}% [%%%%%%%%..]")
        print(f"Still loading...")
    elif level_bar == 9:
        print(f"{level}% [%%%%%%%%%.]")
        print(f"Still loading...")
    elif level_bar == 10:
        print(f"{level}% Complete!")
        print(f"[%%%%%%%%%%]")
    return ""


level = int(input())
print(loading_bar(level))
