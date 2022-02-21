steps = input()
counter_steps = 0
while counter_steps < 10000:
    if steps == 'Going home':
        steps = int(input())
        counter_steps += steps
        break
    
    steps = int(steps)
    counter_steps += steps
    if counter_steps < 10000:
        steps = input()
    

if counter_steps >= 10000:
    steps_over = counter_steps - 10000
    print (f'Goal reached! Good job!\n{steps_over} steps over the goal!')

else:
    steps_under = 10000 - counter_steps
    print (f'{steps_under} more steps to reach goal.')




