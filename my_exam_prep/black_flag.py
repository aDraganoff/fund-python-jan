number_of_days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
the_plunder = 0

for day in range(1, number_of_days+1):
    the_plunder += daily_plunder
    if day % 3 == 0:
        the_plunder += daily_plunder * 0.5
    if day % 5 == 0:
        the_plunder -= the_plunder * 0.3

if the_plunder < expected_plunder:
    needed_plunder = (the_plunder * 100) / expected_plunder
    print(f"Collected only {needed_plunder:.2f}% of the plunder.")
else:
    print(f"Ahoy! {the_plunder:.2f} plunder gained.")

