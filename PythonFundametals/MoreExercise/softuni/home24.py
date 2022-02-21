money_needed = float(input())
money_have = float(input())
counter_days = 0 
counter_spend = 0 
money_sum = 0
while counter_spend != 5:
    action = input()
    m = float(input())
    counter_days += 1

    if action == "spend":
        money_have -= m
        counter_spend += 1
    if money_have < 0:
        money_have = 0 
    if action == 'save':
        money_have += m
        if money_have >= money_needed:
            print (f'You saved the money for {counter_days} days.')
            break

if counter_spend == 5: 
    print (f"You can't save the money.\n{counter_days}")

       