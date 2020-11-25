score_1 = float(input("what score did you get with your first dart?: "))
score_2 = float(input("what score did you get with your second dart?: "))
score_3 = float(input("what score did you get with your third dart?: "))

total_score = score_1 + score_2 + score_3
far_off = 180 - total_score
print(f"with your 3 dart scores you were {far_off} points off the max which is 180")