team_A = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_B = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
cards = input().split()
stop_game = False
for i in cards:
    if i in team_A:
        team_A.remove(i)
    elif i in team_B:
        team_B.remove(i)

    if len(team_A) < 7 or len(team_B) < 7:
        stop_game = True
        break

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if stop_game:
    print(f"Game was terminated")
