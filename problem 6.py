
'''
Two teams score goals each.

If team1 scores more than team2
then print 'win' change the points to 3
and print the number of points.

If both score the same, print 'draw' and change points to 1.
and print the points. Otherwise print lose and print the points.

For example:

Enter Team 1 goals: 2
Enter Team 2 goals: 0
Win
3 points

Enter Team 1 goals: 1
Enter Team 2 goals: 2
Lost
0 points

Enter Team 1 goals: 1
Enter Team 2 goals: 1
Draw
1 point

'''
# Put code below
team1_score = int(input("enter the score of team 1"))
team2_score = int(input("enter the score of team 2"))
team1_point = 0

if team1_score > team2_score:
    print("win")
    team1_point = team1_point + 3
    print(team1_point)
    
if team1_score == team2_score:
    print("draw")
    team1_point = team1_point + 1
    print(team1_point)
    
if team1_score < team2_score:
    print("lost")
    team1_point = 0
    print(team1_point)
    

