n = int(input())
cars_in = set()

for _ in range(n):

    command = input().split(', ')
    operation, car = command

    if operation == 'IN':
        if car not in cars_in:
            cars_in.add(car)

    else:
        if car in cars_in:
            cars_in.remove(car)

if cars_in:
    [print(c) for c in cars_in]

else:
    print('Parking Lot is Empty')
