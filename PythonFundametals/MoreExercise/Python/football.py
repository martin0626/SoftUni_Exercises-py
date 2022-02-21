team = input()
match = int(input())
points = 0
difference = 0
sum_goal = 0
for x in range (match):
    goal_in = int(input())
    goal_out = int(input())
    if goal_in > goal_out:
        points += 3
    elif goal_in == goal_out:
        points += 1
    else:
        points += 0
    sum_goal = goal_in - goal_out
    sum_goal = abs(sum_goal)
    
    
    difference += sum_goal
if points == 0:
     print (f'{team} has been eliminated from the group phase\nGoal difference is -{difference}')

else:
    print (f'{team} finished the group phase with {points} points.\nGoal difference is {difference}')
    
