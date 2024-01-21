number_of_snowballs = int(input())
best_ball = [0,0,0,0]

for current_snowball in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    result = int((weight / time) ** quality)
    if result > best_ball[3]:
        best_ball[0] = weight
        best_ball[1] = time
        best_ball[2] = quality
        best_ball[3] = result
print(f"{best_ball[0]} : {best_ball[1]} = {best_ball[3]} ({int(best_ball[2])})")
