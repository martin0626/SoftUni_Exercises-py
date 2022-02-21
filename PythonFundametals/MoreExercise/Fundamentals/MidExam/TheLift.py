people_waiting = int(input())
state_lift = [int(num) for num in input().split()]
state_after = []
for lift_place in state_lift:
    while lift_place < 4:
        if people_waiting > 0:
            lift_place += 1
        else:
            break
        people_waiting -= 1
    state_after.append(lift_place)


if people_waiting > 0:
    state_after = [str(x) for x in state_after]
    print(f"There isn't enough space! {people_waiting} people in a queue!\n{' '.join(state_after)}")

elif people_waiting == 0 and (len(state_after) * 4) == sum(state_after):
    print (*state_after)

else:
    state_after = [str(x) for x in state_after]
    print (f"The lift has empty spots!\n{' '.join(state_after)}")
    