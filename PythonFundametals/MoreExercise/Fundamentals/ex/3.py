from math import floor
num_comp = int(input())
most_flyes = -10000000000
name =''

for x in range (num_comp):
    comp_name = input()
    passengers = input()
    passangers_for_one = 0
    average = 0
    counter = 0
    while passengers != 'Finish':
        passengers = int(passengers)
        passangers_for_one += passengers
        counter += 1
        passengers = input()
        if passengers == 'Finish':
            average = floor(passangers_for_one / counter)
            

    
    print (f'{comp_name}: {average} passengers.')
    if average > most_flyes:
        most_flyes = average
        name = comp_name

print (f'{name} has most passengers per flight: {most_flyes}')

