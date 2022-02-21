trips_sea = int(input())
trips_mountain = int(input())
type_trip = input()
sum_all = 0
counter_sea = 0
counter_mountain = 0
profit = 0
while type_trip != 'Stop':
    if type_trip == 'sea':
        if counter_sea != trips_sea:
            counter_sea += 1
            profit += 680
        else:
            profit += 0
    elif type_trip == 'mountain':
        if counter_mountain != trips_mountain:
            counter_mountain += 1
            profit += 499
        else:
            profit += 0

    if counter_mountain == trips_mountain and counter_sea == trips_sea:
        print ('Good job! Everything is sold.')
        break
    type_trip = input()
print (f'Profit: {profit} leva.')




