n = int(input())

cars = {}

for _ in range (n):
    car, mileage, fuel = input().split('|')
    mileage = int(mileage)
    fuel = int(fuel)
    if car not in cars:
        cars[car] = {'mileage': mileage, 'fuel': fuel}


command = input()

while command != 'Stop':
    command = command.split(' : ')

    if command[0] == 'Drive':
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])

        if cars[car]['fuel'] >= fuel:
            cars[car]['fuel'] -= fuel
            cars[car]['mileage'] += distance

            print (f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        else:
            print (f"Not enough fuel to make that ride")
        if cars[car]['mileage'] >= 100000:
            print (f'Time to sell the {car}!')
            del cars[car]
    elif command[0] == 'Refuel':

        car = command[1]
        fuel = int(command[2])

        cars[car]['fuel'] += fuel
        if cars[car]['fuel'] > 75:
            fuel =int(command[2]) - (cars[car]['fuel'] - 75) 
             
            cars[car]['fuel'] = 75
        print (f"{car} refueled with {fuel} liters")

    else:
        car = command[1]
        kms = int(command[2])
        cars[car]['mileage'] -= kms

        if cars[car]['mileage'] < 10000:
            cars[car]['mileage'] = 10000
        else:
            print (f"{car} mileage decreased by {kms} kilometers")
    command = input()       
            
cars = dict(sorted(cars.items(), key = lambda x: (-x[1]['mileage'], x[0])))
for car_name in cars.keys():
    print (f"{car_name} -> Mileage: {cars[car_name]['mileage']} kms, Fuel in the tank: {cars[car_name]['fuel']} lt.")



    