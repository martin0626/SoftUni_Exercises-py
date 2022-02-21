exp_needed = float(input())
battles_count = int(input())
exp_sum = 0
done = False
for battle in range (1, battles_count + 1):
    exp_earned = float(input())
    if battle % 3 == 0:
        exp_sum += exp_earned + (exp_earned * 0.15)
    elif battle  % 5 == 0:
        exp_sum += exp_earned - (exp_earned * 0.1)
    else:
        exp_sum += exp_earned
    if exp_sum >= exp_needed:
        print (f'Player successfully collected his needed experience for {battle} battles.')
        done = True
        break

if done == False:
    exp_needed -= exp_sum
    print (f'Player was not able to collect the needed experience, {exp_needed:.2f} more needed.')
